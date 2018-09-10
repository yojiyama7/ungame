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

if __name__ == "__main__":
	
	for question in take_questions():
		print(question.text)

	print(take_token())