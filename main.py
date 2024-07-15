from quiz_brain import Quizbrain
from question_model import Question
from data import question_data
import random

question_count = 0
score = 0
done_question = []

while question_count != 10:
    random_data = random.choice(question_data)

    while random_data not in done_question:
        done_question.append(random_data)
        que_data = random_data["text"]
        ans_data = random_data["answer"]

        question_count += 1
        question = Question(que_data, question_count)
        question.display_question()

        guess = input("").title()
        q_brain = Quizbrain(ans_data)
        if q_brain.check_answer(guess):
            score += 1

        print(f"The correct answer is: {q_brain.answer}")
        print(f"Your current score is: {score} / {question_count} ")
        print(question_count, "\n"*2)

    else:
        random_data = random.choice(question_data)

print("You've completed the quiz.")
print(f"Your final score is: {score } / {question_count}")
