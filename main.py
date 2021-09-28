from question import Question
from user import User
import random
questions = []

def question(number_of_question):
    if number_of_question <4:
        power = 1
    elif number_of_question <8:
        power = 2
    elif number_of_question ==8:
        power = 3
    q1 = random.choice(questions)
    while q1.get_power() != power:
        question()
    print("Next question of our competition: ", q1.get_contents(), "\n\n")
    print("Answer_A: ", q1.get_answers[0])
    print("Answer_B: ", q1.get_answers[1])
    print("Answer_C: ", q1.get_answers[2])
    print("Answer_D: ", q1.get_answers[3], "\n")
    your_answer= input("Your answer is: ")
    if your_answer.upper() == q1.get_correct():
        number_of_question +=1
        question()



def new_game():
    number_of_question = 0


    print()

