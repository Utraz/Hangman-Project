import random

def choose_random_word(word_list):
    """Choose a random word from the list."""
    return random.choice(word_list)

def get_user_input():
    """Prompt the user to enter a single letter and return it."""
    return input("Please enter a single letter: ")

def validate_guess(guess):
    """Check if the input is a single letter."""
    return len(guess) == 1 and guess.isalpha()

def main():
    # List of words to choose from
    word_list = ["Mango", "Strawberry", "Blueberry", "Pineapple", "Watermelon"]
    
    # Choose a random word
    word = choose_random_word(word_list)
    print(f"The chosen word is: {word}")
    
    # Get user input
    guess = get_user_input()
    
    # Validate the user input
    if validate_guess(guess):
        print("Good guess!")
    else:
        print("Oops! That is not a valid input. Please enter a single alphabetical letter.")

# Run the main function
if __name__ == "__main__":
    main()
