import random
import time

# Hint function
def provide_hint(number, guess):
    if number % 2 == 0:
        return "Hint: The number is even."
    else:
        return "Hint: The number is odd."

def get_difficulty_level():
    print("\nPlease select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")
    
    while True:
        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                return 10, "Easy"
            elif choice == 2:
                return 5, "Medium"
            elif choice == 3:
                return 3, "Hard"
            else:
                print("Invalid choice, please select again.")
        except ValueError:
            print("Please enter a valid number.")

def play_game(high_score):
    print("\nWelcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Set the difficulty level and get the number of chances
    chances, level_name = get_difficulty_level()
    print(f"\nGreat! You have selected the {level_name} difficulty level.")
    print(f"\nYou have {chances} chances to guess the correct number.")

    # Randomly select a number between 1 and 100
    number = random.randint(1, 100)
    attempts = 0
    start_time = time.time()  # Start the timer

    hint_used = False

    while attempts < chances:
        try:
            guess = int(input("\nEnter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        attempts += 1

        if guess == number:
            end_time = time.time()
            time_taken = round(end_time - start_time, 2)
            print(f"\nCongratulations! You guessed the correct number {number} in {attempts} attempts.")
            print(f"It took you {time_taken} seconds.")
            if high_score[level_name] is None or attempts < high_score[level_name]:
                high_score[level_name] = attempts
                print(f"\nNew High Score for {level_name}! You guessed the number in {attempts} attempts.")
            return high_score

        elif guess < number:
            print("Incorrect! The number is greater than", guess)
        else:
            print("Incorrect! The number is less than", guess)

        # Provide a hint after 2 incorrect attempts
        if attempts >= 2 and not hint_used:
            hint = provide_hint(number, guess)
            print(f"\n{hint}")
            hint_used = True

        if attempts == chances:
            print(f"\nSorry, you've run out of chances. The correct number was {number}.")
            return high_score

def main():
    high_score = {"Easy": None, "Medium": None, "Hard": None}
    
    while True:
        high_score = play_game(high_score)
        
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != 'y':
            break

    print("\nThanks for playing the Number Guessing Game!")
    print(f"\nHigh Scores:")
    for level, score in high_score.items():
        if score is not None:
            print(f"{level}: {score} attempts")
        else:
            print(f"{level}: No score yet")

if __name__ == "__main__":
    main()
