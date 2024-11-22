"""
Booleans
Coding Exercise: Booleans
SyntheSoda
"""

#### ---- SETUP ---- ####

## -- Menu -- ##

# Print a menu with all the available flavors (see the
# Assignment Panel)

print("Your available soda syrups are: ")
print("  cola")
print("  cherry")
print("  lemon-lime")
print("  orange")
print("  rootbeer")
print("  none")
print()
# --> RUN YOUR CODE <-- #


## -- Variables -- ##

# Create a boolean variable for each flavor and start
# them all as False


cola = False
cherry = False
lemon_lime = False
orange = False
rootbeer = False

## -- User selections -- ##

# Get the user's two flavors as strings

f1 = input("Enter your 1st flavor choice: ")
f2 = input("Enter your 2nd flavor choice: ")
print()

# --> RUN YOUR CODE <-- #

#### ---- RECORD FLAVORS ---- ####

## -- Flavors for either input -- ##

# For each flavor, if either of the user's two strings
# matches that flavor, then set that flavor's variable
# to True

if f1 == "cola" or f2 == "cola":
    cola = True
if f1 == "cherry" or f2 == "cherry":
    cherry = True
if f1 == "lemon-lime" or f2 == "lemon-lime":
    lemon_lime = True
if f1 == "orange" or f2 == "orange":
    orange = True
if f1 == "rootbeer" or f2 == "rootbeer":
    rootbeer = True
    # --> RUN YOUR CODE <-- #


## -- Single syrup - none and anything else -- ##

# Set a boolean variable for whether the user chose
# "none" for one flavor but not both

one_syrup = (f1 == "none" or f2 == "none") and not (f1 == "none" and f2 == "none")

#### ---- FLAVOR OUTPUTS ---- ####

# Print an introduction for the user's flavor

print("Let's try the drink you designed...")
print("Hmmm...")
# Using the boolean variables, print special messages
# for each of the combinations listed in the Assignment
# Panel, and a generic message for everything else

if not cola and not cherry and not lemon_lime and not orange and not rootbeer:
    print("You are just drinking seltzer water. Congratulations on finding the hidden healthy option!")
elif f1 == f2:
    print("You must really like " + f1 + " flavor, huh?")
elif one_syrup:
    print("You have made a normal soda. A little plain, but nothing wrong with that.")
    # --> RUN YOUR CODE <-- #

elif lemon_lime and orange:
    print("This Citrus Blast soda is a masterpiece of refreshing crispness!")
elif cherry and cola:
    print("Congrats, you just made Cherry Coke")
elif cherry and (lemon_lime or orange):
    print("Cherry Citrus: a fruity mixture with surprising depths.")
elif cherry and rootbeer:
    print("Cherry Rootbeer! Avant-garde! A new twist on a comforting classic!")
else:
    print("This combination was a bold choice, but hopefully you will still like it.")

# --> RUN YOUR CODE <-- #

# --> TURN-IN YOUR CODE <-- #
