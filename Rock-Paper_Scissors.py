import random

def get_full_word(letter):
    if letter == 'r':
        return "rock"
    elif letter == 'p':
        return "paper"
    elif letter == 's':
        return "scissors"

def play_game():
    while True:
        player_choice = input("Rock, paper or scissors? (r/p/s): ").lower()

        if player_choice not in ['r', 'p', 's']:
            print("Invalid input. Please choose r, p, or s.")
            continue

        computer_choice = random.choice(['r', 'p', 's'])

        print(f"You chose: {get_full_word(player_choice)}")
        print(f"Computer chose: {get_full_word(computer_choice)}")

        if player_choice == computer_choice:
            print("It's a tie!")

        elif (player_choice == 'r' and computer_choice == 's') or \
             (player_choice == 's' and computer_choice == 'p') or \
             (player_choice == 'p' and computer_choice == 'r'):
            print("You win!")
        else:
            print("You lose!")

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

play_game()
