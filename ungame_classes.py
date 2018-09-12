import random

class Question:
	"""
	id_num: int
	text: str
	"""
	def __init__(self, text):
		self.text = text

with open("../ungame_token.txt", "r", encoding="utf-8") as f:
	_token = f.readline()
with open("questions.txt", "r", encoding="utf-8") as f:
	_lines = f.read().split("\n")
_questions = [Question(line) for line in _lines]

def take_token():
	return _token
def take_questions():
	return _questions

class Phrase:
	def __init__(self, key, text):
		self.key = key
		self.text = text
	
	def set_key(self, key):
		self.key = key
	def set_phrase(self, phrase):
		self.text = text

class PhraseList:
	def __init__(self, phrases):
		self.phrases = [Phrase(*phrase) for phrase in phrases]
	
	def get_by_key(self, key):
		return list(filter(lambda x: x.key==key, self.phrases))[0]
	def get_by_text(self, text):
		return list(filter(lambda x: x.text==text, self.phrases))[0]
	def get_keys(self):
		return [phrase.key for phrase in self.phrases]
	def get_texts(self):
		return [phrase.text for phrase in self.phrases]

class Ungame:
	def __init__(self):
		self.phrase = PhraseList([("join", "join"), ("next", "next")])
		self.questions = take_questions()
		random.shuffle(self.questions)
		self.state = False

	def open(self):
		self.state = "open"
		self.users = []
		return "募集を開始しました。"
	def join(self, user):
		self.users.append(user)
		return f"{user.name}さんが参加しました。"
	def question(self):
		question = self.questions.pop()
		return f"{question.text}\n{self.users[self.user_num].name}さん答えてください。"
	def start(self):
		if self.state != "playing":
			if len(self.users) != 0:
				self.user_num = 0
				self.state = "playing"
				return "ゲームを開始します。\n" + self.question()
			else:
				return "参加者がいません。"
		return "すでにゲームが開始されています。"
	def next(self, user):
		if self.state == "playing":
			if self.users[self.user_num] == user:
				self.user_num = (self.user_num+1) % len(self.users)
				return "--------\n" + self.question()
	def end(self):
		self.state = False
		return "ゲームを終了しました。"
	def command(self, message):
		command = message.content
		if "/" == command[0]:
			cmd = command[1:].split(" ")
			if "ungame" == cmd[0]:
				if "phrase" == cmd[1]:
					return self.set_phrase(cmd[2], cmd[3])
				elif "open" == cmd[1]:
					return self.open()
				elif "start" == cmd[1]:
					return self.start()
				elif "stop" == cmd[1]:
					return self.end()
		elif command in self.phrase.get_texts():
			phrase_key = self.phrase.get_by_text(command).key
			if "join" == phrase_key:
				return self.join(message.author)
			elif "next" == phrase_key:
				return self.next(message.author)

class UngameList:
	def __init__(self, ungames=dict()):
		self.ungames = ungames
	def __getitem__(self, key):
		return self.ungames[key]

	def add_ungame(self, key):
		self.ungames[key] = Ungame()
	def pop_ungame(self, key):
		self.ungames.pop(key)
	def command(self, message):
		channel = message.channel
		if channel not in self.ungames:
			self.add_ungame(channel)
		return self[channel].command(message)

if __name__ == "__main__":

	for question in take_questions():
		print(question.text)

	print(take_token())