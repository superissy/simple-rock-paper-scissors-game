#!/usr//bin/python3
import random
import os
#This is a Rock Paper Scissors game between a user or player and a computer 
# The computer choices are stored inside a list container 
# The users choice are stored inside an input variable 
# The Random function is chosen to randomly pick for the computer 
# An If logic function check if Computers choice and users choice are Tie or wrong to decide the Winner 

# #function to clear the screen
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
# list to stocre greeting message{
welcome_note = {
                'Game FAQ :': 'Rock beats Scissors, Scissors beats Paper, Paper beats Rock',
                1:'You will Choose from Rock, Paper or Scissors', 
                2:'Computer will Randomly choose Game', 
                3:'The winner will be decided by the rules of the game',
                4:'Good Luck and Have Fun'
                }


#function to get the user name
def print_header():
    print('--------------------------------')
    print('  Create username to start game')
    print('--------------------------------')
    print()
print_header()

#varaible to store the user name
username = str(input('Enter your username: '))
#To capitalize the first letter of the username
username = username.capitalize()

#Function paraemeters to clear the screen.
cls()

#Function to print the header and welcome message
def greetings_header():
    print()
    print()
    print('*'*50)
    print(username,'Welcome to Rock, Paper & Scissors Game')
    print('*'*50)
    print()
    for key, Value in welcome_note.items():
        print(key, Value)
        print()
    # print('Good Luck', username)
    print()
greetings_header()
print()

#computer choices stored in a list container
computer_choice = ['SCISSORS', 'ROCK', 'PAPER']

#Numbers of rounds to play
trial = int(input('How many rounds do you want to play? '))
cls()
print('*'*50)
print(username,'You have chosen', trial, 'rounds  of game to play')
print('*'*50)
print()

#If logic function to check if Computers choice and users choice are Tie or wrong to decide the Winner
while trial > 0:
    #Create a list of Choices for the computer and using random moduls (Choice) to pick each choices
    computer_choices = random.choice(computer_choice)
    #user choice stored in a variable
    user_choice = str(input('Do you want - Rock, Paper, or Scissors?: '))
    user_choice = user_choice.upper()
    cls()
    print()
    if computer_choices == user_choice:
        print(username, " It's a TIE You have chosen", user_choice, 'and Computer has chosen', computer_choices)
        trial -= 1
        print("You have ", trial, " Games left")
        print()

    elif user_choice == 'ROCK' and computer_choices == 'SCISSORS':
        print(username, " YOU WIN !!! | You Chose", user_choice, 'and Computer has chosen', computer_choices)
        trial -= 1
        print("You have ", trial, " Games left")
        print()

    elif user_choice == 'PAPER' and computer_choices == 'ROCK':
        print(username, " YOU WIN !!! | You Chose", user_choice, 'and Computer has chosen', computer_choices)
        trial -= 1
        print("You have ", trial, " Games left")
        print()

    elif user_choice == 'SCISSORS' and computer_choices == 'PAPER':
        print(username, " YOU WIN !!! | You Chose", user_choice, 'and Computer has chosen', computer_choices)
        trial -= 1
        print("You have ", trial, " Games left")
        print()
    else:
        print("Sorry", username, " You lose !!! | You Chose", user_choice, 'and Computer has chosen', computer_choices)
        trial -= 1
        print("You have ", trial, " Games left")
        print()

    if trial == 0:
        print("Game Over - You have no more Games left...")
        break