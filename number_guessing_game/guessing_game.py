import random
import math

def main():
    print("Hi! Welcome to the Number Guessing Game.")

    def get_int_input(prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid input! Please enter an integer.")
                return get_int_input(prompt)

    first_number = get_int_input("Please input first number of range: ")

    last_number = get_int_input("Please input last number of range: ")
    if first_number >= last_number:
        print("Invalid range! Last number should be bigger then first number.")
        last_number = get_int_input("Please input last number of range: ")

    random_number = random.randint(first_number, last_number)
    user_number = None
    chances = math.ceil(math.log(last_number - first_number + 1, 2))
    guesses = 0

    print(f"\nYou have {chances} chances to guess the number between {first_number} and {last_number}. Let's start!")

    while guesses < chances:
        user_number = get_int_input(f"Please input your number between {first_number} and {last_number}: ")
        if user_number < first_number or user_number > last_number:
            print(f"Your number is out of range! Please input a number between {first_number} and {last_number}.")
            continue
        guesses += 1
        if guesses >= chances and user_number != random_number:
            print(f"Sorry! You have used all your chances. The number was {random_number}.")
        elif user_number < random_number:
            print("Your number is too small!")
        elif user_number > random_number:
            print("Your number is too big!")
        else:
            print("Congratulations! You guessed the number! \nIt took you", guesses, "guesses.")
            break