
import random

# Write a program that consists of a game of rock, paper, scissors against the computer.
# The player can select rock, paper, or scissors by typing the word into the console and be warned if they type anything else.
# At each round, the player must enter an option and be informed if they won, lost, or tied.
# At the end of the round, player can select if he wants to play again or not.
# Display the player score at the end of the game.
# The game should be able to handle both upper and lower case inputs.
# The computer should randomly select rock, paper, or scissors.
# The game should handle invalid inputs and prompt the user to enter a valid input.
# The game should display the computer's choice and the player's choice at the end of each round.
# The game should display the final score at the end of the game.
# The game should display the winner at the end of the game.


print('Welcome to Rock, Paper, Scissors')

player_score = 0
computer_score = 0

while True:
    player_choice = input('Enter rock, paper, or scissors: ')
    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    if player_choice.lower() not in ['rock', 'paper', 'scissors']:
        print('Invalid input. Please enter rock, paper, or scissors.')
        continue

    print(f'Player choice: {player_choice}')
    print(f'Computer choice: {computer_choice}')

    if player_choice.lower() == computer_choice:
        print('Tie!')
    elif player_choice.lower() == 'rock' and computer_choice == 'scissors':
        print('Player wins!')
        player_score += 1
    elif player_choice.lower() == 'paper' and computer_choice == 'rock':
        print('Player wins!')
        player_score += 1
    elif player_choice.lower() == 'scissors' and computer_choice == 'paper':
        print('Player wins!')
        player_score += 1
    else:
        print('Computer wins!')
        computer_score += 1

    print(f'Player score: {player_score}')
    print(f'Computer score: {computer_score}')

    play_again = input('Do you want to play again? (yes/no): ')
    if play_again.lower() != 'yes':
        break

    