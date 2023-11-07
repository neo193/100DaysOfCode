from questionmodel import Question
from data import question_data

question_bank = []

for i in range(0, len(question_data)):
    objCreate = Question(question_data[i]["text"], question_data[i]["answer"])
    question_bank.append(objCreate)

print(question_bank[0].question)
