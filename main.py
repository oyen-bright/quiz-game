from question_model import Question
from data import question_data
from  quiz_brain import QuizBrain

question_bank = [Question(question['text'],question['answer']) for question in question_data]

Quiz = QuizBrain(question_bank)

while Quiz.still_has_question():
    Quiz.next_question()

print("You've completed the Qize")
print(f"Your final score is {Quiz.score}/{Quiz.question_number}")