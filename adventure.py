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

# As a game developer I want to have a option checker
# so that we can prevent a user to select invalid options

# As a game developer I want to have a fight with
# enemies so that the game can be challenging

# As a game developer I want to have an option to
# escape the enemy so that a user won't die (game over)
