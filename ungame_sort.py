with open("questions.txt", "r", encoding="utf-8") as f:
    questions = f.read().split("\n")

while "" in questions:
    questions.remove("")

question_lists = []
for question in questions:
    id_num, text = question.split("|")
    question_lists.append([int(id_num), question])

question_lists.sort()

questions_sorted = map(lambda x: x[1], question_lists)

with open("questions_sorted.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(questions_sorted))
