from question import Question
from user import User
import random
questions = []
users = []
win = [0, 1000, 2000, 5000, 10000, 20000, 100000, 250000, 10000000]
def question(number_of_question, win, x):
    if number_of_question <4:
        power = 1
    elif number_of_question <8:
        power = 2
    elif number_of_question ==8:
        power = 3
    q1 = random.choice(questions)
    while q1.get_power() != power:
        question(number_of_question, win, x)
    print("Your win is: ", win[number_of_question-1])
    print("Next question of our competition: ", q1.get_contents(), "\n\n")
    print("Answer_A: ", q1.get_answers[0])
    print("Answer_B: ", q1.get_answers[1])
    print("Answer_C: ", q1.get_answers[2])
    print("Answer_D: ", q1.get_answers[3], "\n")
    print("If you want to end our game print 'PASS'")
    your_answer= input("Your answer is: ")
    if your_answer.upper() == q1.get_correct() and number_of_question!=7:
        number_of_question +=1
        question(number_of_question, win, x)
    elif your_answer.upper() == "PASS":
        users[x-1].set_wins(users[x-1].get_wins()+win[number_of_question])
        print("Congratulation! You've won ", win[number_of_question], "Now you have ", users[x-1].get_wins(), "$" )
    elif your_answer.upper() != q1.get_correct():
        print("Unfortunetelly it is not correct answer ;/ Try again and good lunck next time!")
        if number_of_question == (1, 2, 3):
            number_of_question == 1
        elif number_of_question == (4, 5, 6, 7):
            number_of_question == 4
        print("Congratulation! You've won ", win[number_of_question], "Now you have ", users[x-1].get_wins(), "$" )
    elif  your_answer.upper() == q1.get_correct() and number_of_question==7:
        users[x-1].set_wins(users[x-1].get_wins()+win[number_of_question+1])
        print("Congratulation! You've won ", win[number_of_question+1],"You are the best!!!. Now you have ", users[x-1].get_wins(), "$" )

def create_new_user(users):
    print("Here you can create a new user\n\n")
    login = input("Write login: ")
    password = input("Write password with one capital letter: ")
    users.append(User(login, password))

def create_question(questions):
    Question.get_answers
    power = int(input("Write power 1, 2 or 3 of this question: "))
    contents = input("Write contents of this question: ")
    answerA = input("Write first answer: ")
    answerB = input("Write second answer: ")
    answerC = input("Write third answer: ")
    answerD = input("Write fourth answer: ")
    correct = input("Which one is correct? A B C or D")
    questions.append(Question(power, contents, [answerA, answerB, answerC, answerD], correct))

def see_users(users):
    for x in range(1, len(users)+1):
        print(x, "-", users[x].get_login(), "games: ", users[x].get_games(), "wins: ", users[x].get_wins())


def get_account(users, number_of_question):
    login = input("login: ")
    for x in range(1, len(users)):
        if login == users[x-1].get_login():
            password = input("password: ")
            if users[x-1].get_password() ==password:
                question(number_of_question, win, x)
        else:
            menu_1(users, questions, number_of_question)

    

def menu_1(users, questions, number_of_question):
    print("""
    MAIN MANU
    
    1 - start a new game
    2 - create a new user
    3 - see list of users
    4 - delete an user
    0 - return""")

    click = int(input("What do you choose: "))
    if click == 1:
        get_account(users, number_of_question)
        menu_1(users, questions, number_of_question)
    elif click == 2:
        create_new_user(users)
        menu_1(users, questions, number_of_question)
    elif click == 3:
        see_users(users)
        menu_1(users, questions, number_of_question)
    






def new_game():
    number_of_question = 0
    win = 0
    question(number_of_question, win)

    print()

