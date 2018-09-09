import random

class Question:
	def __init__(self, id_num, text):
		self.id_num = id_num
		self.text = text

if __name__ == "__main__":

	with open("questions.txt", "r", encoding="utf-8") as f:
		lines = f.read().split("\n")

	while "" in lines:
		lines.remove("")
	
	questions = []
	for line in lines:
		id_num, text = line.split("|")
		questions.append(Question(int(id_num), text))

	random.shuffle(questions)
	for question in questions:
		print(question.text)