# milestone_3.py
# Step 1: Define the check_guess function
def check_guess(letter, word):
    """
    Check if the guessed letter is in the word.
    Args:
        letter (str): The guessed letter.
        word (str): The word to guess.
    """
    letter = letter.lower()  # Ensure the guess is in lowercase

    # Check if the letter is in the word
    if letter in word:
        print(f"Good guess! '{letter}' is in the word.")
    else:
        print(f"Sorry, '{letter}' is not in the word. Try again.")


# Step 2: Define the get_user_input function
def get_user_input():
    """
    Continuously prompts the user for a valid single letter input.
    Returns:
        str: A single valid letter.
    """
    while True:
        user_input = input("Please enter a single letter: ")
        if len(user_input) == 1 and user_input.isalpha():
            return user_input.lower()  # Return valid input in lowercase
        else:
            print("Invalid input. Please enter a single alphabetical character.")


# Step 3: Define the play_game function
def play_game(word):
    """
    Manages the flow of the word guessing game.
    Args:
        word (str): The word to guess.
    """
    while True:
        guess = get_user_input()  # Get a valid guess from the user
        check_guess(guess, word)  # Check if the guess is correct
        # You can add break logic here if you want to end the game after correct guesses


# Run the game
if __name__ == "__main__":
    word_to_guess = "example"
    play_game(word_to_guess)
