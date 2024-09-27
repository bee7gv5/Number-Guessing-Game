# Number-Guessing-Game

The **Number Guessing Game** is a simple command-line interface (CLI) based game where the computer randomly selects a number between 1 and 100, and the player must guess the number within a limited number of attempts based on the selected difficulty level. The game features multiple rounds, a timer, a hint system, and high-score tracking, making it an engaging and fun experience.

# Features
## Difficulty Levels:

- Easy (10 chances)
- Medium (5 chances)
- Hard (3 chances)

 ### Gameplay Mechanics:

- The player guesses a number, and the game provides feedback on whether the number is higher or lower.
- A **hint system** provides a clue after two incorrect guesses.
- **High Score:** Tracks the fewest number of attempts taken to guess the number for each difficulty level.
- **Multiple Rounds:** The player can choose to play multiple rounds until they decide to quit.
- **Timer:** Tracks how long the player takes to guess the correct number.

## Installation
1. Clone the repository or download the project files:
   ```bash
   git clone https://github.com/bee7gv5/Number-Guessing-Game.git

2. Navigate to the project directory:
   ```bash
   cd number-guessing-game
3. Run the game:
   ```bash
   python3 game.py

## How to Play

1. When the game starts, you will be prompted to select a difficulty level:
   - Easy (10 attempts)
   - Medium (5 attempts)
   - Hard (3 attempts)
2. The computer will randomly select a number between 1 and 100, and you will have to guess the number within the given number of attempts.

3. After each incorrect guess, the game will let you know whether the number is higher or lower than your guess.

4. If you guess incorrectly twice, a hint will be provided.

5. The game will display the time taken to guess the number and the number of attempts after each successful round.

6. After completing a round, you can choose to play again or exit.

## Example Gameplay
```bash
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.

Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)

Enter your choice: 2

Great! You have selected the Medium difficulty level.
You have 5 chances to guess the correct number.

Enter your guess: 50
Incorrect! The number is less than 50.

Enter your guess: 30
Incorrect! The number is greater than 30.

Hint: The number is even.

Enter your guess: 40
Congratulations! You guessed the correct number 40 in 3 attempts.
It took you 10.5 seconds.

New High Score for Medium! You guessed the number in 3 attempts.

Do you want to play again? (y/n): n

Thanks for playing the Number Guessing Game!
```

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/bee7gv5/Number-Guessing-Game/blob/main/LICENSE) file for details.

## Acknowledgments

Sample solution for the [Number Guessing Game](https://roadmap.sh/projects/number-guessing-game) challenge from [roadmap.sh](https://roadmap.s).

   
