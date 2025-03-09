import random
import illustrations.illustrations

def game_choice():
    print('1. Scissors\n2. Rock\n3. Paper \n')
    choice = int(input('Enter your choice: '))
    options = ['scissors', 'rock', 'paper']
    user_choice = options[choice - 1]
    computer_choice = random.choice(options)
    return user_choice, computer_choice

def main():
    print("Let's play Rock-Paper-Scissors!")
    user_score = 0
    cpu_score = 0

    for round in range(1, 4):
        print(f'\nRound {round} \n')
        user_choice, computer_choice = game_choice()
        print(f'\nYou chose: ')
        print(getattr(illustrations.illustrations, user_choice)())
        print(f'The computer chose: ')
        print(getattr(illustrations.illustrations, computer_choice)())

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'scissors' and computer_choice == 'rock') or \
                (user_choice == 'rock' and computer_choice == 'paper') or \
                (user_choice == 'paper' and computer_choice == 'scissors'):
            cpu_score += 1
        else:
            user_score += 1

        print(f'You: {user_score}, Computer: {cpu_score}')

    if user_score > cpu_score:
        print(illustrations.illustrations.winner())
    elif cpu_score > user_score:
        print(illustrations.illustrations.loser())
    else:
        print(illustrations.illustrations.tie())

main()