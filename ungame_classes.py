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

class Deck:
	def __init__(self, questions):
		self.questions = random.shuffle(questions)

	def draw(self):
		return self.questions.pop()
	def is_empty(self):
		return self.questions == []

class Ungame:
	def __init__(self):
		self.deck = Deck()
	
	def start(self, players):
		self.players = players
		self.player_num = 0
		self.next()

	def next(self):
		if self.deck.is_empty():
			return False
		else:
			question = self.deck.draw()
			player = self.players[self.player_num]
			self.player_num += 1
			return "to " + player.name + "\n" + question.text

if __name__ == "__main__":

	for question in take_questions():
		print(question.text)

	print(take_token())