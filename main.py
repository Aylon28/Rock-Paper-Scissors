import random


def get_rating_from_file(user_name):
    with open('rating.txt', 'r') as f:
        for line in f:
            name, rating = line.split()
            if name == user_name:
                return int(rating)
    return 0


def get_the_user_win(user_choice, computer_choice):
    beat_options = {
        'rock': ['fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge'],
        'fire': ['scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper'],
        'scissors': ['snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air'],
        'snake': ['human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water'],
        'human': ['tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon'],
        'tree': ['wolf', 'sponge', 'paper', 'air', 'water', 'dragon', 'devil'],
        'wolf': ['sponge', 'paper', 'air', 'water', 'dragon', 'devil', 'lightning'],
        'sponge': ['paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun'],
        'paper': ['air', 'water', 'dragon', 'devil', 'lightning', 'gun', 'rock'],
        'air': ['water', 'dragon', 'devil', 'lightning', 'gun', 'rock', 'fire'],
        'water': ['dragon', 'devil', 'lightning', 'gun', 'rock', 'fire', 'scissors'],
        'dragon': ['devil', 'lightning', 'gun', 'rock', 'fire', 'scissors', 'snake'],
        'devil': ['lightning', 'gun', 'rock', 'fire', 'scissors', 'snake', 'human'],
        'lightning': ['gun', 'rock', 'fire', 'scissors', 'snake', 'human', 'tree'],
        'gun': ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf']
    }
    if computer_choice in beat_options[user_choice]:
        return True
    else:
        return False


def main():
    choices = ['rock', 'paper', 'scissors']           # options we are playing with
    print('Enter your name:', end=' ')
    user_name = input()
    user_rating = get_rating_from_file(user_name)
    print('Hello,', user_name)
    rules = input()
    if len(rules) > 0:
        choices += rules.split(',')                   # updating game options (should be from 'beat_options' dictionary
    print('Okay, let\'s start')
    user_choice = input()

    while user_choice != '!exit':
        computer_choice = random.choice(choices)
        if user_choice in choices:
            computer = choices.index(computer_choice)
            user = choices.index(user_choice)
            if computer == user:
                print(f'There is a draw ({user_choice})')
                user_rating += 50
            else:
                if get_the_user_win(user_choice, computer_choice):
                    print(f'Well done. The computer chose {computer_choice} and failed')
                    user_rating += 100
                else:
                    print(f'Sorry, but the computer chose {computer_choice}')
        elif user_choice == '!rating':
            print('Your rating:', user_rating)
        else:
            print('Invalid input.')
        user_choice = input()

    print('Bye!')


if __name__ == '__main__':
    main()
