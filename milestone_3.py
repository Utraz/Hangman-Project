# milestone_3.py

# Step 1: Define the check_guess function
def check_guess(guess, word):
    # Step 2: Convert the guess to lower case
    guess = guess.lower()

    # Step 3: Check if the guess is in the word
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

# Step 1: Define the ask_for_input function
def ask_for_input(word):
    while True:
        # Step 2: Ask the user to guess a letter
        guess = input("Please enter a single letter: ")

        # Step 3: Check that the guess is a single alphabetical character
        if len(guess) == 1 and guess.isalpha():
            # Step 4: Call the check_guess function
            check_guess(guess, word)
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

# Outside the function, call the ask_for_input function to test the code
def main():
    word = "example"  # The word to guess
    ask_for_input(word)

# Run the main function
if __name__ == "__main__":
    main()

