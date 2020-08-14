import random

global weapon_level

# As a game developer I want to have random
# enemies so that a user won't be bored.
def enemy():
    enemy = random.choice(["dragon", "gorgon", "wicked fairie", "troll"])
    return enemy

# As a game developer I want to have a mistery
# weapon so that a user can get excited with
# different levels of dificulty.
def init():
    global weapon_level
    weapon_level = 0

# As a user I want to have some dramatic pauses
# during the game so that can be more exciting
def print_pause(text):
    print(text)
    time.sleep(2)

# As a game developer I want to have a option checker
# so that we can prevent a user to select invalid options

# As a game developer I want to have a fight with
# enemies so that the game can be challenging

# As a game developer I want to have an option to
# escape the enemy so that a user won't die (game over)

def main():
    # Things that happen when the game starts
    init()
    print_pause("You find yourself standing in an open field, \
filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {active_enemy} is somewhere\
around here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very\
effective) dagger.")
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    option = input("What would you like to do?\n(Please enter 1 or 2).\n")
    while option_validation(option) is False:
        option = input()
    if(option == "1"):
        house()
    else:
        cave()
