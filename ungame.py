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
	questions = [Question(*line.split("|")) for line in lines]

	for question in random.shuffle(questions):
		print(question.text)