import random

target_amount = int(input("Hur många måltavlor vill du ha? "))
targets = [0]*target_amount
shots_taken = 0


# Prints an intro with formatted text to the console
def intro():
    row_length = 50
    print(
f"""
{'~'*row_length}
{'Biathlon'.center(row_length)}
{'a hit or miss game'.center(row_length)}
{'~'*row_length}
""")


# Prints the board to the console
def print_board():
    print(*range(1, target_amount+1))
    print(*['*' if i == 0 else 'O' for i in targets])


def take_shot(position):
    global shots_taken
    shots_taken += 1
    hit_or_miss = random.randint(0, 1)

    # Target was hit
    if hit_or_miss:
        # Target was previously hit
        if targets[position]:
            print("Hit on closed target")
        # Target has not been hit previously
        else:
            print("Hit on open target")
            targets[position] = 1
    # Target was not hit
    else:
        print("Miss")
    print()


# Takes care of asking for input and
def prompt_shot():
    position = int(input(f'Shot nr {shots_taken+1} at: ')) - 1
    take_shot(position)



def restart_game():
    global targets
    global shots_taken
    prompt_restart = input("Vill du starta om? (y/N)")
    if prompt_restart.lower() == 'y':
        targets = [0] * target_amount
        shots_taken = 0
        return True

    return False


def game():
    intro()
    first_round = True
    while first_round or restart_game():
        first_round = False
        print(f'You got {target_amount} shots\n')
        while shots_taken < target_amount:
            print_board()
            prompt_shot()
        print_board()
        print(f"You hit {sum(targets)} of {len(targets)} targets")

    return



game()