import random

with open("../ungame_token.txt", "r", encoding="utf-8") as f:
	token = f.readline()
def take_token():
	return token

class Question:
	"""
	id_num: int
	text: str
	"""
	def __init__(self, text):
		self.text = text

with open("questions.txt", "r", encoding="utf-8") as f:
	lines = f.read().split("\n")
questions = [Question(line) for line in lines]
def take_questions():
	return questions

if __name__ == "__main__":
	
	for question in take_questions():
		print(question.text)

	print(take_token())