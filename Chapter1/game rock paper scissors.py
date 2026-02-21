#import Librarys
import random

#import and global variables
USER_CHOICE= ("rock","paper","scissors")

#create a function to get user input
def get_user_input():
    choice=input("pick your choice [\"rock\",\"paper\",\"scissors\"]:")
    while choice not in USER_CHOICE:
        choice=input("pick your choice [\"rock\",\"paper\",\"scissors\"]:")
    return choice

#create a function to get pc input
def get_pc_input():
    pc_choice = random.choice(USER_CHOICE)
    print(f"pc choise was: {pc_choice}")
    return pc_choice

#compare and determine which on is the winner
def determine_winner(user_input,pc_input):
    if user_input == pc_input:
        return "draw!"
    elif user_input == "rock" and pc_input == "scissors"\
        or (user_input == "scissors" and pc_input == "paper")\
        or (user_input == "paper" and pc_input == "rock"):
        print("user won!")
    else:
        print("computer won")
#creat a main function as the runner
def main():
    user_input = get_user_input()
    pc_input = get_pc_input()
    determine_winner(user_input,pc_input)
    print("end of peogram")

#make an intration for doing the game as much as we need

answer = "y"
while answer == "y":
    main()
    answer = input("do you want to continue?! (y/n):")