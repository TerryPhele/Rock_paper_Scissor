import random

def get_user_choice():
    user_choice=''
    while True:
        user_choice=input('Enter 1. for rock, 2. for paper, 3. for scissors, exit to stop the game: ')
        if (user_choice.isnumeric() and is_valid(user_choice)) or  (user_choice.casefold())== 'exit':
            break
    if user_choice.isnumeric():
        return int(user_choice)
    return user_choice #incase of exit


def is_valid(input):
    if int(input) in range(1,4):
        return True
    return False


def get_computer_choice():
    computer_choice = random.randint(1,3)
    return computer_choice


def evaluate_results(computer_choice, user_choice,counters=[0,0,0]):
    choice=(computer_choice,user_choice)
    if choice ==(1,3) or choice == (2,1) or choice == (3,2):
        counters[0]= counters[0]+1  #increment number of computer_wins
        display_results('Computer')
    elif choice ==(1,2) or choice ==(2,3) or choice == (3,1):
        counters[1]= counters[1]+1  #increment number of user_wins
        display_results('You')
    elif  choice ==(1,1) or choice ==(2,2) or choice == (3,3):
        counters[2]= counters[2]+1  #increment number of draws
        display_results('draw')
    return counters


def display_results(player):
    if player == 'draw':
        print("Its a draw")
    else:
        print(f'{player} win.')

def show_game_statistic(computer_wins, user_wins,draws):
    print(f"""-----GAME STATISTICS-----
--------------------------------------
    |Computer    |   User    |   draw
--------------------------------------
Tot |           {computer_wins}|          {user_wins}|      {draws}""")

def run_game():
    print("WELCOME TO ROCK,PAPER,SCISSOR".center(50,"-"))
    print()
    user_choice='0'
    computer_choice=''
    user_counter=0
    computer_counter=0
    draw_counter=0

    while user_choice:
        user_choice=get_user_choice()
        computer_choice=get_computer_choice()
        computer_counter,user_counter, draw_counter = evaluate_results(computer_choice,user_choice,
                                                                        [computer_counter,user_counter,draw_counter])
        if str(user_choice).casefold() == 'exit':
            show_game_statistic(computer_counter,user_counter,draw_counter)
            print('\nExiting the game:')
            break
        print("\nNew turn")

if __name__ == "__main__":
    run_game()
