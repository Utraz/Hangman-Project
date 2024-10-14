#milestone_5.py

import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        """
        Initializes the Hangman game with the given word list and number of lives.

        Args:
            word_list (list): A list of words to choose from.
            num_lives (int): The number of lives the player has at the start of the game (default is 5).
        """
        self.word_list = word_list
        self.secret_word = random.choice(word_list)  # Pick a random word from the word list
        self.guessed_word = ['_' for _ in self.secret_word]  # Initialize the guessed word with underscores
        self.remaining_unique_letters = len(set(self.secret_word))  # Count unique letters in the word
        self.remaining_lives = num_lives  # Set the number of lives
        self.guessed_letters = []  # List to store guesses already made

    def update_guessed_word(self, letter):
        """
        Update the guessed word with the correctly guessed letter.

        Args:
            letter (str): The correctly guessed letter.
        """
        for index, char in enumerate(self.secret_word):
            if char == letter:
                self.guessed_word[index] = letter

    def check_guess(self, letter):
        """
        Check if the guessed letter is in the word and update the game state.

        Args:
            letter (str): The guessed letter.
        """
        letter = letter.lower()  # Ensure the guess is in lowercase

        if letter in self.secret_word:
            print(f"Good guess! '{letter}' is in the word.")
            self.update_guessed_word(letter)  # Update the guessed_word list
            self.remaining_unique_letters -= 1  # Decrease unique letters count
        else:
            print(f"Sorry, '{letter}' is not in the word. Try again.")
            self.remaining_lives -= 1  # Decrease lives if the guess is incorrect
            
        # Print the number of lives left
        print(f"You have {self.remaining_lives} lives left.")

    def get_user_input(self):
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

    def play_round(self):
        """
        Plays one round of the game by asking the user for input and processing the guess.
        """
        print(f"\nCurrent word: {' '.join(self.guessed_word)}")
        guess = self.get_user_input()  # Get a valid guess from the user

        if guess in self.guessed_letters:
            print(f"You've already guessed '{guess}'. Try again.")
        else:
            self.guessed_letters.append(guess)  # Add the guess to the list
            self.check_guess(guess)  # Check if the guess is correct


def play_game(word_list):
    """
    Orchestrates the Hangman game.

    Args:
        word_list (list): The list of possible words to guess.
    """
    num_lives = 5  # Set number of lives
    game = Hangman(word_list, num_lives)  # Instantiate the Hangman game

    # Loop to control the flow of the game
    while True:
        if game.remaining_lives == 0:
            print('You lost!')
            break  # End the game if no lives are left

        if game.remaining_unique_letters > 0:
            game.play_round()  # Continue the game and ask for input
        else:
            print('Congratulations. You won the game!')
            break  # End the game if all letters have been guessed


# Run the game
if __name__ == "__main__":
    words = ["apple", "banana", "cherry", "date", "elderberry"]
    play_game(words)

