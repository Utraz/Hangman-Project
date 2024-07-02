import random

word_list = ["Mango", "Strawberry", "Blueberry", "Pineapple", "Watermelon"]
word = random.choice(word_list)
print(word)

# Ask the user to enter a single letter and assign it to the variable 'guess'
guess = input("Please enter a single letter: ")

# Check if the input is a single letter
if len(guess) == 1 and guess.isalpha():
    print(f"Good guess!")
else:
    print("Oops! That is not a valid input.")
