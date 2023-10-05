import random

targets = [0]*5
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
    print(*range(1, len(targets)+1))
    print(*['*' if i == 0 else 'O' for i in targets])


def handle_shot():
    global shots_taken
    shots_taken += 1
    position = int(input(f'Shot nr {shots_taken} at: ')) - 1

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


def game():
    intro()
    print(f'You got {len(targets)} shots\n')
    while shots_taken < len(targets):
        print_board()
        handle_shot()
    print_board()
    print(f"You hit {sum(targets)} of {len(targets)} targets")
    return

game()