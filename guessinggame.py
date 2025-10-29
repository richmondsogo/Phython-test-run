import sys
import random

# Set the default range
start_number_int = 30
end_number_int = 36

# Check for command-line arguments
# sys.argv[0] is the script name itself, so we need at least 3 elements
if len(sys.argv) >= 3:
    try:
        # Override default range with user-provided arguments
        start_number_int = int(sys.argv[1])
        end_number_int = int(sys.argv[2])
    except ValueError:
        print("Invalid command-line arguments. Using default range (30-36).")

# Loop the game until the user guesses correctly
while True:
    correct_number = random.randint(start_number_int, end_number_int)
    
    while True:
        try:
            guess = int(input(f'Guess a number between {start_number_int} and {end_number_int}: '))
            
            if guess == correct_number:
                print('You are a genius!')
                break  # Exit the inner guessing loop
            else:
                print('Wrong number. Try again.')
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    # Ask the user if they want to play again
    play_again = input('Do you want to play again? (yes/no): ').lower()
    if play_again != 'yes':
        break  # Exit the outer game loop

print("Thanks for playing!")
