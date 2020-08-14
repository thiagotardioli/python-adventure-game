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

def cave():
    # Things that happen to the player goes in the cave
    global weapon_level
    if weapon_level == 0:
        weapon_level = 1
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take\
the sword with you.")
        print_pause("You walk back out to the field.")
        print_pause("Enter 1 to knock on the door of the house.")
        print_pause("Enter 2 to peer into the cave.")
        option = input("What would you like to do?\n")
        while option_validation(option) is False:
            option = input()
        if(option == "1"):
            house()
        else:
            cave()
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before, and gotten\
all the good stuff. It's just an empty cave now.")
        print_pause("You walk back out to the field.\n")
        print_pause("Enter 1 to knock on the door of the house.")
        print_pause("Enter 2 to peer into the cave.")
        option = input("What would you like to do?\
\n(Please enter 1 or 2.)\n")
        while option_validation(option) is False:
            option = input()
        if(option == "1"):
            house()
        else:
            cave()


# As a user I want to have some dramatic pauses
# during the game so that can be more exciting
def print_pause(text):
    print(text)
    time.sleep(2)

# As a game developer I want to have a option checker
# so that we can prevent a user to select invalid options

# As a game developer I want to have a fight with
# enemies so that the game can be challenging
def fight():
    # Things that happen when the player fights
    if weapon_level == 0:
        print_pause("You do your best...")
        print_pause(f"but your dagger is no match for the {active_enemy}.")
        print_pause("You have been defeated!")
        gameover()
    else:
        print_pause(f"As the {active_enemy} moves to attack,\
you unsheath your new sword.")
        print_pause("The Sword of Ogoroth shines brightly in your\
hand as you brace yourself for the attack.")
        print_pause(f"But the {active_enemy} takes one look at your\
shiny new toy and runs away!")
        print_pause(f"You have rid the town of the {active_enemy}.\
You are victorious!")
        gameover()

def house():
    # Things that happen to the player in the house
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to knock when the door\
opens and out steps a {active_enemy}.")
    print_pause(f"Eep! This is the {active_enemy}'s house!")
    print_pause(f"The {active_enemy} attacks you!")
    if weapon_level == 0:
        print_pause("You feel a bit under-prepared for this,\
what with only having a tiny dagger.")
    option = input("Would you like to (1) fight or (2) run away?\n")
    while option_validation(option) is False:
        option = input()
    if(option == "1"):
        fight()
    else:
        field()

# As a game developer I want to have an option to
# escape the enemy so that a user won't die (game over)
def field():
    # Things that happen when the player runs back to the field
    print_pause("You run back into the field. Luckily,\
you don't seem to have been followed.\n")
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    option = input("What would you like to do?\n(Please enter 1 or 2.)\n")
    while option_validation(option) is False:
        option = input()
    if(option == "1"):
        house()
    else:
        cave()

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
