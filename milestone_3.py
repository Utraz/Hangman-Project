# milestone_3.py

def main():
    while True:
        # Step 2: Ask the user to guess a letter
        guess = input("Please enter a single letter: ")

        # Step 3: Check that the guess is a single alphabetical character
        if len(guess) == 1 and guess.isalpha():
            # Step 4: If the guess passes the checks, break out of the loop
            print("Good guess!")
            break
        else:
            # Step 5: If the guess does not pass the checks, print a message
            print("Invalid letter. Please, enter a single alphabetical character.")

# Run the main function
if __name__ == "__main__":
    main()
