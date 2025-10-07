import random
def play_game():
    name = input("What is your name? ")
    print(f"Hello, {name}! Welcome to the Word Guessing Game.")
    words = ['rainbow', 'computer', 'science', 'programming',
             'python', 'mathematics', 'player', 'condition',
             'reverse', 'water', 'board', 'geeks']
    word = random.choice(words)
    print("Guess the characters")
    guesses = ''
    turns = 12
    while turns > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char, end=' ')
            else:
                print("_", end=' ')
                failed += 1
        if failed == 0:
            print("\nYou Win")
            print(f"The word is: {word}")
            break
        guess = input("\nGuess a character: ")
        guesses += guess
        if guess not in word:
            turns -= 1
            print("Wrong")
            print(f"You have {turns} more guesses")
            if turns == 0:
                print("You Lose")
                print(f"The word was: {word}")

