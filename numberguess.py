# --- Number Guessing Game ---
# This is a simple game where the computer picks a number
# and the user has to guess it.

# We need the 'random' library to help the computer pick a random number.
import random

def guessing_game():
    """This function contains the main logic for the game."""

    print("---------------------------------------")
    print("  Welcome to the Number Guessing Game! ")
    print("---------------------------------------")
    print("I'm thinking of a number between 1 and 50.")
    print("Can you guess what it is?\n")

    # Generate a random integer between 1 and 50.
    # The computer will store this number in the 'secret_number' variable.
    secret_number = random.randint(1, 50)
    
    # We'll keep track of how many guesses the user has made.
    guess_count = 0
    max_guesses = 6 # Let's give the user 6 chances.

    # This 'while' loop will continue as long as the user has guesses left.
    while guess_count < max_guesses:
        # This line asks the user for their guess and stores it.
        # The 'int()' part converts the user's text input into a whole number.
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            # This 'except' block catches the error if the user types something that isn't a number.
            print("Oops! That's not a valid number. Please try again.")
            continue # This skips the rest of the loop and asks for input again.

        # Increment the guess counter.
        guess_count += 1

        # Now, we use 'if/elif/else' to check the guess.
        if guess < secret_number:
            print("Too low! Try a higher number.")
        elif guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            # If the guess is not higher or lower, it must be correct!
            print(f"\n🎉 Congratulations! You guessed the number {secret_number} correctly!")
            print(f"It took you {guess_count} guesses.")
            break # This 'break' keyword exits the loop since the game is won.

        # Let the user know how many guesses they have left.
        guesses_left = max_guesses - guess_count
        if guesses_left > 0:
            print(f"You have {guesses_left} guesses left.\n")

    # This 'if' statement runs only if the 'while' loop finishes without the user guessing correctly.
    if guess_count == max_guesses and guess != secret_number:
        print("\n😢 Game Over! You've run out of guesses.")
        print(f"The number I was thinking of was {secret_number}.")

# --- This is the standard way to run the main function in a Python script ---
if __name__ == "__main__":
    guessing_game()

