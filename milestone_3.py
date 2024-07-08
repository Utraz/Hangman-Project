# milestone_3.py

def main():
    word = "example"  # The word to guess
    while True:
        # Step 2: Ask the user to guess a letter
        guess = input("Please enter a single letter: ")

        # Step 3: Check that the guess is a single alphabetical character
        if len(guess) == 1 and guess.isalpha():
            # Step 1: Check if the guess is in the word
            if guess in word:
                # Step 2: Print a message if the guess is in the word
                print(f"Good guess! {guess} is in the word.")
                break
            else:
                # Step 3: Print a message if the guess is not in the word
                print(f"Sorry, {guess} is not in the word. Try again.")
        else:
            # Step 5: If the guess does not pass the checks, print a message
            print("Invalid letter. Please, enter a single alphabetical character.")

# Run the main function
if __name__ == "__main__":
    main()

