class QuizBrain:

    def __init__(self, qList):
        self.questionNumber = 0
        self.questionList = qList
        self.score = 0

    def hasQuestions(self):
        if self.questionNumber < len(self.questionList):
            return True
        else:
            print(f"You've completed the quiz!\nYour final score is {self.score}/{self.questionNumber}")
            return False

    def nextQuestion(self):
        currentQuestion = self.questionList[self.questionNumber]
        self.questionNumber += 1
        answer = input(f"Q.{self.questionNumber}: {currentQuestion.text} (True/False): ")
        self.checkAnswer(answer, currentQuestion.answer)

    def checkAnswer(self, answer, correctAnswer):
        if answer.lower() == correctAnswer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correctAnswer}")
        print(f"Your current score is: {self.score}/{self.questionNumber}")
        print("\n")
