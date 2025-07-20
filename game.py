import random
import time
import sys

player_name = input('Enter your name: ')
print(f'\n------Welcome to Snake-Water-Gun Game {player_name}-------')

rules = '\nRules of the game: \n 1. Snake and Gun -> Gun \n 2. Snake and Water -> Snake \n 3. Gun and Water -> Water'
player_options = '\nYou should choose one of the following options: \n s for Snake🐍 \n w for Water💦 \n g for Gun🔫'
quit_option = '\nPlay as many rounds you want and when you are done, press q to quit the game'

print(rules)
print(player_options)
print(quit_option)

def processing_dot_animation(message='processing', delay=0.5):
    print(message, end='', flush=True)
    for i in range(3):
        print('.', end='', flush=True)
        time.sleep(delay)
    print()

player_points = []
computer_points = []
options = ['s', 'w', 'g']
round_number = 1
no_of_ties = 0

while True:
    computer_choice = random.choice(options)
    print(f'\n_-_-_-_-_Round {round_number}-_-_-_-_'.center(80))
    player_choice = input('\nEnter your choice: ')

    if player_choice == 's' and computer_choice == 'w':
        processing_dot_animation()
        print('Your choice: Snake🐍')
        print('Computer choice: Water💦\n')
        print(f'Winner of the round: {player_name}👏🎉')
        player_points.append(1)
        round_number += 1

    elif player_choice == 's' and computer_choice == 'g':
        processing_dot_animation()
        print('Your choice: Snake🐍')
        print('Computer choice: Gun🔫\n')
        print('Winner of the round: Computer🤖🎉')
        computer_points.append(1)
        round_number += 1

    elif player_choice == 'w' and computer_choice == 'g':
        processing_dot_animation()
        print('Your choice: Water💦')
        print('Computer choice: Gun🔫\n')
        print(f'Winner of the round: {player_name}👏🎉')
        player_points.append(1)
        round_number += 1

    elif player_choice == 'w' and computer_choice == 's':
        processing_dot_animation()
        print('Your choice: Water💦')
        print('Computer choice: Snake🐍\n')
        print('Winner of the round: Computer🤖🎉')
        computer_points.append(1)
        round_number += 1

    elif player_choice == 'g' and computer_choice == 's':
        processing_dot_animation()
        print('Your choice: Gun🔫')
        print('Computer choice: Snake🐍\n')
        print(f'Winner of the round: {player_name}👏🎉')
        player_points.append(1)
        round_number += 1

    elif player_choice == 'g' and computer_choice == 'w':
        processing_dot_animation()
        print('Your choice: Gun🔫')
        print('Computer choice: Water💦\n')
        print('Winner of the round: Computer🤖🎉')
        computer_points.append(1)
        round_number += 1

    elif player_choice == computer_choice:
        equal_sign = '🟰'
        processing_dot_animation()
        print('Your choice:', 'Snake🐍' if player_choice == 's' else 'Water💦' if player_choice == 'w' else 'Gun🔫')
        print('Computer choice:', 'Snake🐍' if computer_choice == 's' else 'Water💦' if computer_choice == 'w' else 'Gun🔫')
        print('\n')
        print(f'This round is a tie {equal_sign}')
        print('You both will get no points for this round')
        round_number += 1
        no_of_ties += 1

    elif player_choice == 'q':
        print('_------You have quit the game------_\n')

        if sum(player_points) > sum(computer_points):
            print('Congratulations!🎉')
            print('You have won the game🥳')
            print('Your total score: ', sum(player_points))
            print("Computer's total score: ", sum(computer_points))
            print('Total number of ties: ', no_of_ties)
            print('You were ahead of computer by', sum(player_points) - sum(computer_points), 'points👏')
            print('Here is your award; a 🏆🏆🏆\n')
            print('Thank you for playing the game!😊')

        elif sum(player_points) < sum(computer_points):
            print('Computer has won the game😎')
            print('You have lost😓')
            print('Your score: ', sum(player_points))
            print("Computer's score: ", sum(computer_points))
            print('Total number of ties: ', no_of_ties)
            print('Better luck next time🍀')

        elif sum(player_points) == sum(computer_points):
            print('The game is a tie🟰')
            print('You both have earned', sum(player_points), 'points👏🟰')

        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again == 'y':
            player_points.clear()
            computer_points.clear()
            round_number = 1
            no_of_ties = 0
            continue
        else:
            print("\nThanks for playing! 👋")
            break

    else:
        print('Invalid input❌')
        print('Please enter a valid input')
