class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score=0
        self.question_list=question_list

    def next_question(self):
        new_question = (self.question_list[self.question_number])
        self.question_number +=1
        user_answer= input(f"Q.{self.question_number}: {new_question.text} (True/False) ?")
        self.check_answer(user_answer, new_question.answer)

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, question_answer):
        if user_answer.lower() == question_answer.lower():
            self.score += 1
            print("you got it right")
        else:
            print("you got it wrong")
        print(f"Tne correct answer was: {question_answer}")
        print(f"The current score is {self.score}/{self.question_number}")
        print("\n")

