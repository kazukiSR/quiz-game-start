from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questionBank = []
for currentQ in question_data:
    questionBank.append(Question(currentQ["question"], currentQ["correct_answer"]))

quiz = QuizBrain(questionBank)
while quiz.hasQuestions():
    quiz.nextQuestion()
