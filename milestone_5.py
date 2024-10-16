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
        self.secret_word = random.choice(word_list)
        self.guessed_word = ['_' for _ in self.secret_word]
        self.remaining_unique_letters = len(set(self.secret_word))
        self.remaining_lives = num_lives
        self.guessed_letters = []

    def _update_guessed_word(self, letter):
        """
        Private method to update the guessed word with the correctly guessed letter.

        Args:
            letter (str): The correctly guessed letter.
        """
        for index, char in enumerate(self.secret_word):
            if char == letter:
                self.guessed_word[index] = letter

    def _process_correct_guess(self, letter):
        """
        Handles the scenario when the guessed letter is correct.

        Args:
            letter (str): The correctly guessed letter.
        """
        print(f"Good guess! '{letter}' is in the word.")
        self._update_guessed_word(letter)
        self.remaining_unique_letters -= 1

    def _process_incorrect_guess(self, letter):
        """
        Handles the scenario when the guessed letter is incorrect.

        Args:
            letter (str): The incorrectly guessed letter.
        """
        print(f"Sorry, '{letter}' is not in the word. Try again.")
        self.remaining_lives -= 1

    def _check_guess(self, letter):
        """
        Check if the guessed letter is in the word and update the game state.

        Args:
            letter (str): The guessed letter.
        """
        if letter in self.secret_word:
            self._process_correct_guess(letter)
        else:
            self._process_incorrect_guess(letter)
        print(f"You have {self.remaining_lives} lives left.")

    def _get_valid_input(self):
        """
        Continuously prompts the user for a valid single letter input.

        Returns:
            str: A valid lowercase letter.
        """
        while True:
            user_input = input("Please enter a single letter: ").lower()
            if len(user_input) == 1 and user_input.isalpha():
                return user_input
            else:
                print("Invalid input. Please enter a single alphabetical character.")

    def _is_repeated_guess(self, guess):
        """
        Check if the guessed letter has already been guessed.

        Args:
            guess (str): The letter guessed by the player.

        Returns:
            bool: True if the letter has been guessed before, False otherwise.
        """
        return guess in self.guessed_letters

    def play_round(self):
        """
        Plays one round of the game by asking the user for input and processing the guess.
        """
        print(f"\nCurrent word: {' '.join(self.guessed_word)}")
        guess = self._get_valid_input()

        if self._is_repeated_guess(guess):
            print(f"You've already guessed '{guess}'. Try again.")
        else:
            self.guessed_letters.append(guess)
            self._check_guess(guess)


def play_game(word_list):
    """
    Orchestrates the Hangman game.

    Args:
        word_list (list): The list of possible words to guess.
    """
    game = Hangman(word_list)

    while game.remaining_lives > 0 and game.remaining_unique_letters > 0:
        game.play_round()

    if game.remaining_lives == 0:
        print('You lost!')
    else:
        print('Congratulations. You won the game!')


if __name__ == "__main__":
    word_list = ["apple", "banana", "cherry", "date", "elderberry"]
    play_game(word_list)
