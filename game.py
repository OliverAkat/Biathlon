import random

# Variables used throughout the game to track progress
target_amount = int(input("Hur många måltavlor vill du ha? "))
skill = int(input("Hur skicklig är du? 1-5 "))
energy = 5
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

def validate_skill():
    global skill

    if skill > 5:
        skill = 5
    elif skill < 1:
        skill = 1


def update_energy(energy_1):
    energy_1 -= 1
    if energy_1 == 0:
        energy_1 = 1
    return energy_1
# Takes care of taking the shot at a given target
def take_shot(position):
    global shots_taken
    global energy
    shots_taken += 1
    hit_or_miss = random.randint(-5, 5) + skill - (5-energy)

    energy = update_energy(energy)
    
    # Target was hit
    if hit_or_miss >= 0:
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


def validate_shot(shot):
    try:
        shot = int(shot)
    except:
        return 0    

    if shot >= target_amount:
        return (target_amount - 1)
    elif shot < 1:
        return 1
    return shot - 1

# Prompts input and takes the shot
def handle_shot():
    position = (input(f'Shot nr {shots_taken+1} at: ')) 
    
    take_shot(validate_shot(position))


# Prompts restart and resets parameters
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
    validate_skill()
    # Makes sure the game does not ask for a restart
    # before the first round (the conditional statement
    # does not check the second condition if the first one is true)
    first_round = True
    while first_round or restart_game():
        first_round = False
        print(f'You got {target_amount} shots\n')
        while shots_taken < target_amount:
            print_board()
            handle_shot()
        print_board()
        print(f"You hit {sum(targets)} of {len(targets)} targets")

    return




game()