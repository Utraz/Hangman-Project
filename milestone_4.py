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
            self.update_guessed_word(letter)  # Update the word_guessed list
            self.remaining_unique_letters -= self.secret_word.count(letter)  # Decrease unique letters count
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

    def play_game(self):
        """
        Manages the flow of the word guessing game.
        """
        while self.remaining_lives > 0 and self.remaining_unique_letters > 0:
            print(f"\nCurrent word: {' '.join(self.guessed_word)}")
            print(f"Lives left: {self.remaining_lives}")
            guess = self.get_user_input()  # Get a valid guess from the user
            
            if guess in self.guessed_letters:
                print(f"You've already guessed '{guess}'. Try again.")
                continue
            
            self.guessed_letters.append(guess)  # Add the guess to the list
            self.check_guess(guess)  # Check if the guess is correct
            
            if self.remaining_unique_letters == 0:  # All letters guessed
                print(f"Congratulations! You've guessed the word: {self.secret_word}")
                break
        else:
            print(f"Game over! The word was: {self.secret_word}")

# Run the game
if __name__ == "__main__":
    words = ["apple", "banana", "cherry", "date", "elderberry"]
    hangman_game = Hangman(words)
    hangman_game.play_game()
