import os
questions = "/Users/arlun/Desktop/programming/python/discord_bot/ungame/questions.txt"

with open(questions) as before_q_file:
    questions_str = before_q_file.read()

questions_list = questions_str.split("\n")

while "\n" in questions_list:
    questions_list.remove("\n")

for i,l in enumerate(questions_list):
    l = l.split("|")
    questions_list[i] = [int(l[0]), l[1]]

questions_list.sort()

for i,l in enumerate(questions_list):
    l[0] = str(l[0])
    questions_list[i] = "|".join(l)

with open("/Users/arlun/Desktop/programming/python/discord_bot/ungame/questions_sorted", mode = "w") as after_q_file:
    after_q_file.write("\n".join(questions_list))
