#imports and globals variables
import random

Max_num = 10
Min_num = 1
# max_number_count = 3

#generate a random number
def generate_random_number():
    return random.randint(Min_num,Max_num)

#add user input as guess
def get_user_input():
    print(f"your number should be between {Min_num} -{Max_num}")
    while True:
        try:
            user_input = int(input("Enter your guess: "))
        except ValueError:
            print("Error! Enter a valid number!")
        else:
            return user_input
        
#check guessed number
def check_guess_number(user_input,random_num):
    return user_input == random_num

#main function for runnig application
def main():
    max_number_count = 3
    random_num = generate_random_number()
    print(f"random number is: {random_num}")
    while max_number_count > 0:
        user_input = get_user_input()
        if check_guess_number(user_input,random_num):
            print("you have guessed right!")
            break
        max_number_count-=1
        print(f"guess left: {max_number_count}")
    else:
        print("you couldn't guess number and ran out of guesses!!!")

#main
if __name__ == "__main__":
    main()
    