# import the random module
import random
print("-------------------------------")
print(" |Welcome to 'PIG' Dice Game!|")
print("-------------------------------\n")

print("\t\tUSER VS COMPUTER\n")
# user_choice = int(input("Enter the no.of players 2-4 : "))
roll_dice = ["""
 ___________________
|                   |
|                   |
|         *         |
|                   |
|___________________|    """, """
 ___________________
|                   |
|      *            |
|                   |
|          *        |
|___________________|    """, """               
 ___________________
|                   |
|   *               |
|         *         |
|              *    |
|___________________|    """, """
 ___________________
|                   |
|    *          *   |
|                   |
|    *          *   |
|___________________|   """, """
 ___________________
|                   |
|  *             *  |
|         *         |
|  *             *  |
|___________________|   """, """
 ___________________
|                   |
|   *            *  |
|   *            *  |
|   *            *  |
|___________________|   """]

# print(roll_dice[user_action])

# ------------------------ This Block of Code runs when any gain 6 ----------------------------


def rolling():

    # turn_roll = roll()
    # print(f'{roll_dice[turn]})
    min_score = 0
    max_score = 4

    while min_score < max_score:
        user_turn = roll()
        comp_turn = roll()
        print(f'\t\tUSER:{roll_dice[user_turn]}\n\t COMPUTER:{roll_dice[comp_turn]}')
        choice_u_c = input('Again play? (y/n): ')
        if choice_u_c.lower() != 'y':
            break
        else:
            pass
        min_score += 1
    print('Reach limit done')

    # Only four attempts are used to get the winner

    if user > computer:
        print(f'User win with score {min_score + user + 1}')
    elif user == computer:
        print(f'Tie with score {min_score + computer + 1}')
    else:
        print(f'Computer win with score {min_score + computer + 1}')
    return "\n | THANKS FOR PLAYING THE GAME |"
# ----------------------------------- End of above part --------------------------------------


def roll():
    minimum_value = 0
    maximum_value = 5
    die = random.randint(minimum_value, maximum_value)
    return die


turn = roll()
# print(f'\t[ Player 1 ] {roll_dice[turn]}\n\n')
while True:
    players = input('Enter the number of players: ')
    if players.isdigit():
        players = int(players)
        if players <= 1:
            print("Don't have enough players, must at least 2 players")
            should_user = input("Do yo want to play again? (y/n): ")
            if should_user.lower() != 'y':
                break
            else:
                print("Let's start the game again\n")
                continue
        elif players > 2:
            print("Only 2 players are allowed")
#            break
            continue
        elif players == 2:
            print("Let's start\n")
        while True:
            user = roll()
            computer = roll()

            print(f"\t\tUSER: {roll_dice[user]}\n\n\t\t VS\n\n\t  COMPUTER: {roll_dice[computer]}\n")

            if user == 5 and computer == 5:
                quit('Tie Game')
            elif user == 5:
                second_roll = input(f"User get 'SIX' so chance to second time roll the dice (y/n): ")
                if second_roll.lower() != 'y':
                    break
                else:
                    print('After new Scrolling to USER\n', roll_dice[turn], '\n')
                    print(rolling())
                    break

            elif computer == 5:
                second_roll = input(f"Computer get 'SIX' so chance to second time roll the dice (y/n): ")
                if second_roll.lower() != 'y':
                    break
                else:
                    print('After new Scrolling to COMPUTER\n', roll_dice[turn], '\n')
                    print(rolling())
                    break

#            elif user == 5 and computer == 5:
#                quit()

            should_user = input("Do yo want to play again? (y/n): ")
            if should_user.lower() != 'y':
                break
            else:
                print("Let start the game again\n")
        break

    else:
        print("Invalid, try again\n")

# --------------------------------------------------------------------------------------------------------------
