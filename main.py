from question import Question
from user import User
import random



questions = []
users = []
win = [0, 1000, 2000, 5000, 10000, 20000, 100000, 250000, 10000000]
number_of_question = 1
def question(number_of_question, win, x, questions):
    #u_login = open("users_login.txt", "r")
    
    if number_of_question <4:
        power = 1
    elif number_of_question <8:
        power = 2
    elif number_of_question ==8:
        power = 3
    q1 = questions[random.randint(0, len[questions]-1)]
    while q1.get_power() != power:
        question(number_of_question, win, x, questions)
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
        question(number_of_question, win, x, questions)
    elif your_answer.upper() == "PASS":
        users[x-1].set_wins(users[x-1].get_wins()+win[number_of_question])
        print("Congratulation! You've won ", win[number_of_question], "Now you have ", users[x-1].get_wins(), "$" )



    elif your_answer.upper() != q1.get_correct():
        print("Unfortunetelly it is not correct answer ;/ Try again and good lunck next time!")
        if number_of_question == (1, 2, 3):
            number_of_question == 1
        elif number_of_question == (4, 5, 6, 7):
            number_of_question == 4
        users[x-1].set_wins(users[x-1].get_wins()+win[number_of_question])
        print("Congratulation! You've won ", win[number_of_question], "Now you have ", users[x-1].get_wins(), "$" )

    elif  your_answer.upper() == q1.get_correct() and number_of_question==7:
        users[x-1].set_wins(users[x-1].get_wins()+win[number_of_question+1])
        print("Congratulation! You've won ", win[number_of_question+1],"You are the best!!!. Now you have ", users[x-1].get_wins(), "$" )

    u_games = open("users_game.txt", "r")
    u_win = open("users_pass.txt", "r")
    wins = u_win.readlines().rstrip('\n')
    wins[x-1] = str(users[x-1].get_wins())
    u_win = open("users_pass.txt", "a")
    u_win.writelines(wins)
    u_win.close()
    games = u_games.readlines().rstrip('\n')
    games[x-1] = str(users[x-1].get_wins())
    u_games = open("users_pass.txt", "a")
    u_games.writelines(wins)
    u_games.close()
    number_of_question = 1

def create_new_user(users):
    u_pass = open("users_pass.txt", "a")
    u_login = open("users_login.txt", "a")
    u_games = open("users_game.txt", "a")
    u_win = open("users_win.txt", "a")
    u_games.writelines(["0", "\n"])
    u_win.writelines(["0", "\n"])
    print("Here you can create a new user\n\n")
    login = input("Write login: ")
    u_login.writelines([login, "\n"])
    password = input("Write password with one capital letter: ")
    u_pass.writelines([password, "\n"])
    users.append(User(login, password))
    u_pass.close()
    u_login.close()

def file_of_login(users):
    u_login = open("users_login.txt", "r")
    u_pass = open("users_pass.txt", "r")
    for login in u_login:
        if login.rstrip('\n') != "":
            password = u_pass.readline().rstrip('\n')
            users.append(User(login.rstrip('\n'), password))

def create_question(questions):
    q_contents = open("question_contents.txt", "a")
    q_answerA = open("question_answerA.txt", "a")
    q_answerB = open("question_answerB.txt", "a")
    q_answerC = open("question_answerC.txt", "a")
    q_answerD = open("question_answerD.txt", "a")
    q_correct = open("question_correct.txt", "a")
    q_power = open("question_power.txt", "a")

    power = input("Write power 1, 2 or 3 of this question: ")
    q_power.writelines([power, "\n"])

    contents = input("Write contents of this question: ")
    q_contents.writelines([contents, "\n"])

    answerA = input("Write first answer: ")
    q_answerA.writelines([answerA, "\n"])

    answerB = input("Write second answer: ")
    q_answerB.writelines([answerB, "\n"])

    answerC = input("Write third answer: ")
    q_answerC.writelines([answerC, "\n"])

    answerD = input("Write fourth answer: ")
    q_answerD.writelines([answerD, "\n"])

    correct = input("Which one is correct? A B C or D")
    q_correct.writelines([correct, "\n"])

    questions.append(Question(power, contents, [answerA, answerB, answerC, answerD], correct))
    for file in (q_contents, q_answerA, q_answerB, q_answerC, q_answerD):
        file.close()

def file_of_question(questions):
    q_contents = open("question_contents.txt", "r")
    q_answerA = open("question_answerA.txt", "r")
    q_answerB = open("question_answerB.txt", "r")
    q_answerC = open("question_answerC.txt", "r")
    q_answerD = open("question_answerD.txt", "r")
    q_correct = open("question_correct.txt", "r")
    q_power = open("question_powers.txt", "r")
    for contents in q_contents:
        if contents != "":
            answerA = q_answerA.readline().rstrip('\n')
            answerB = q_answerB.readline().rstrip('\n')
            answerC = q_answerC.readline().rstrip('\n')
            answerD = q_answerD.readline().rstrip('\n')
            correct = q_correct.readline().rstrip('\n')
            power = q_power.readline().rstrip('\n')
            questions.append(Question(power, contents, [answerA, answerB, answerC, answerD], correct))

def see_users(users):
    for x in range(1, len(users)+1):
        print(x, "-", users[x-1].get_login(), "games: ", users[x-1].get_games(), "wins: ", users[x-1].get_wins())


def get_account(users, number_of_question, questions):
    login = input("login: ")
    for x in range(1, len(users)+1):
        if login == users[x-1].get_login():
            password = input("password: ")
            if users[x-1].get_password() ==password:
                question(number_of_question, win, x, questions)
        else:
            menu_1(users, questions)

    

def menu_1(users, questions):
    print("""
    MAIN MANU
    
    1 - start a new game
    2 - create a new user
    3 - add a new question
    4 - see list of users
    5 - delete an user
    0 - exit""")

    click = int(input("What do you choose: "))
    if click == 1:
        number_of_question = 0
        get_account(users, number_of_question, questions)
        menu_1(users, questions)
    elif click == 2:
        create_new_user(users)
        menu_1(users, questions)
    elif click == 3:
        create_question()
        menu_1(users, questions)
    elif click == 4:
        see_users(users)
        menu_1(users, questions)
    elif click == 5:
        see_users(users)
        delete = int(input("Which one you want to delete? "))
        del users[delete-1]
        menu_1(users, questions)

    




file_of_login(users)
file_of_question(questions)
menu_1(users, questions)
