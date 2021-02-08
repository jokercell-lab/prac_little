from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

#print(question_data[0]["text"])

question_bank = []
for question in question_data:
    q_t = question["question"]
    q_a = question["correct_answer"]
    new_q = Question(q_t, q_a)
    question_bank.append(new_q)

quiz_brain = QuizBrain(question_bank)


while quiz_brain.still_has_question():
    quiz_brain.next_question()
print("You've completed !")
print(f"Your final score is {quiz_brain.score}/{quiz_brain.question_number}")