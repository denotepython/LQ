# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random
def name_to_number(name):
    # delete the following pass statement and fill in your code below
    if name  == 'rock':
        number = 0
    elif name == 'Spock':
        number = 1
    elif name == 'paper':
        number = 2
    elif name == 'lizard':
        number = 3
    elif  name == 'scissors':
        number = 4
    else:
        print 'Error name'

    return number
    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    if number == 0:
        name = 'rock'
    elif number == 1:
        name = 'Spock'
    elif number == 2:
        name = 'paper'
    elif number == 3:
        name = 'lizard'
    elif number == 4:
        name = 'scissors'
    else:
        print 'Error number'

    return name
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
    
    print '\n'
    # print a blank line to separate consecutive games
    print 'Player chooses %s' % player_choice
    # print out the message for the player's choice
    player_number = name_to_number(player_choice)
    # convert the player's choice to player_number using the function name_to_number()
    compute_number = random.randrange(0,5)
    # compute random guess for comp_number using random.randrange()
    compute_name = number_to_name(compute_number)
    # convert comp_number to comp_choice using the function number_to_name()
    print 'Computer chooses %s' % compute_name
    # print out the message for computer's choice
    result = (player_number - compute_number) % 5
    # compute difference of comp_number and player_number modulo five
    if result > 2:
        print 'Computer wins!'
    elif result > 0:
        print 'Player wins!'
    else:
        print 'Tie!'
    # use if/elif/else to determine winner, print winner message

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric

