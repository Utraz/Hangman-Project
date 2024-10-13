#milestone_4.py

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
        self.word = random.choice(word_list)  # Pick a random word from the word list
        self.word_guessed = ['_' for _ in self.word]  # Initialize the guessed word with underscores
        self.num_letters = len(set(self.word))  # Count unique letters in the word
        self.num_lives = num_lives  # Set the number of lives
        self.list_of_guesses = []  # List to store guesses already made

    def check_guess(self, letter):
        """
        Check if the guessed letter is in the word and update the game state.

        Args:
            letter (str): The guessed letter.
        """
        letter = letter.lower()  # Ensure the guess is in lowercase

        if letter in self.word:
            print(f"Good guess! '{letter}' is in the word.")
            # Update the word_guessed list
            for index, char in enumerate(self.word):
                if char == letter:
                    self.word_guessed[index] = letter
            self.num_letters -= self.word.count(letter)  # Decrease unique letters count
        else:
            print(f"Sorry, '{letter}' is not in the word. Try again.")
            self.num_lives -= 1  # Decrease lives if the guess is incorrect
           # Print the number of lives left
        print(f"You have {self.num_lives} lives left.")

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

    def play_game(self):
        """
        Manages the flow of the word guessing game.
        """
        while self.num_lives > 0 and self.num_letters > 0:
            print(f"\nCurrent word: {' '.join(self.word_guessed)}")
            print(f"Lives left: {self.num_lives}")
            guess = self.get_user_input()  # Get a valid guess from the user
            if guess in self.list_of_guesses:
                print(f"You've already guessed '{guess}'. Try again.")
                continue
            
            self.list_of_guesses.append(guess)  # Add the guess to the list
            self.check_guess(guess)  # Check if the guess is correct
            
            if self.num_letters == 0:  # All letters guessed
                print(f"Congratulations! You've guessed the word: {self.word}")
                break
        else:
            print(f"Game over! The word was: {self.word}")

# Run the game
if __name__ == "__main__":
    words = ["apple", "banana", "cherry", "date", "elderberry"]
    hangman_game = Hangman(words)
    hangman_game.play_game()
