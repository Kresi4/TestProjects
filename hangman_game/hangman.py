import random
from collections import Counter

print("Welcome in Hangman Game!")
print("You will be guessing the letters of a hidden word.")

words = ["apple", "banana", "mango", "strawberry",
"orange", "grape", "pineapple", "apricot", "lemon", "coconut", "watermelon",
"cherry", "papaya", "berry", "peach", "lychee", "muskmelon"]

word = random.choice(words)

