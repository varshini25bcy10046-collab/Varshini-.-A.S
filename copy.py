import random

def number_guessing_game():
    """
    A simple number guessing game where the user tries to guess a randomly
    generated number within a specified range.
    """
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess it?")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
                break  # Exit the loop if the guess is correct
        except ValueError:
            print("Invalid input. Please enter a whole number.")

if _name_ == "_main_":
    number_guessing_game()
