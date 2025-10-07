import random

print("Welcome in Rock, Paper, Scissor Game!")
print("You will be playing against computer.")
print("Rock beats Scissor, Scissor beats Paper, Paper beats Rock.")
print("Let's start the game!")

def get_user_choice():
    user_input = input("Enter Rock, Paper or Scissor: ").lower()
    if user_input in ['rock', 'paper', 'scissor']:
        return user_input
    else:
        print("Invalid input! Please enter Rock, Paper or Scissor.")
        return get_user_choice()

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissor'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissor') or \
         (user_choice == 'scissor' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def multiple_rounds():
    rounds = input("How many rounds do you want to play? (default is 1): ")
    if rounds.isdigit() and int(rounds) > 0:
        return int(rounds)
    else:
        print("Invalid input! Defaulting to 1 round.")
        return 1

def play_game():
    rounds = multiple_rounds()
    user_wins = 0
    computer_wins = 0
    ties = 0

    for _ in range(rounds):
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_wins += 1
        elif result == "Computer wins!":
            computer_wins += 1
        else:
            ties += 1

    print(f"\nFinal Results after {rounds} rounds:")
    print(f"You won: {user_wins} times")
    print(f"Computer won: {computer_wins} times")
    print(f"Ties: {ties} times")

    if user_wins > computer_wins:
        print("Overall, you are the champion!")
    elif computer_wins > user_wins:
        print("Overall, computer is the champion!")
    else:
        print("Overall, it's a tie!")

if __name__ == "__main__":
    play_game()


