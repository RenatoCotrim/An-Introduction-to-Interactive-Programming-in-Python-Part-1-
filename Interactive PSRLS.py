# URL = http://www.codeskulptor.org/#user45_t1PTVOxsx6_1.py

# GUI-based version of RPSLS

###################################################
# Student should add code where relevant to the following.

import simplegui
import random

# Functions that compute RPSLS

# helper functions

def name_to_number(name):
# delete the following pass statement and fill in your code below
    if name == "rock":
        number = 0
        return number
    elif name == "Spock":
        number = 1
        return number
    elif name == "paper":
        number = 2
        return number
    elif name == "lizard":
        number = 3
        return number
    elif name == "scissors":
        number = 4
        return number
    else:
        return "Error: Name does not match any of the five correct input strings"

    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
# delete the following pass statement and fill in your code below
    if number == 0:
        name = "rock"
        return name
    elif number == 1:
        name = "Spock"
        return name
    elif number == 2:
        name = "paper"
        return name
    elif number == 3:
        name = "lizard"
        return name
    elif number == 4:
        name = "scissors"
        return name
    else:
        return "Error: Number does not match any of the five correct input"
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    
def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
       
    # print a blank line to separate consecutive games
    print ""
    
    # print out the message for the player's choice
    print "Player chooses "+player_choice
    
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
        
    # compute random guess for comp_number using random.randrange()
    comp_number=random.randrange(0,5,1)
    
    # convert comp_number to comp_choice using the function number_to_name()
    
    # print out the message for computer's choice
    print "Computer chooses " + number_to_name(comp_number)
    
    # compute difference of comp_number and player_number modulo five
    difference = (comp_number - player_number) % 5
    
    # use if/elif/else to determine winner, print winner message
    if difference == 1 or difference == 2:
        print "Computer wins!"
    elif difference == 0:
        print "Player and computer tie!"
    else:
        print "Player wins!"
     
    
# Handler for input field
def get_guess(guess):
    if not (guess == "rock" or guess == "Spock" or
            guess == "paper" or guess == "scissors" or guess == "lizard"):
        print
        print 'Error: Bad input "' + guess + '" to rpsls'
        return
    else:
        rpsls(guess)
    
# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("GUI-based RPSLS", 200, 200)
frame.add_input("Enter guess for RPSLS (hit Enter)", get_guess, 200)


# Start the frame animation
frame.start()


###################################################
# Test

get_guess("Spock")
get_guess("dynamite")
get_guess("paper")
get_guess("lazer")

###################################################
# Sample expected output from test
# Note that computer's choices may vary from this sample.

#Player chose Spock
#Computer chose paper
#Computer wins!
#
#Error: Bad input "dynamite" to rpsls
#
#Player chose paper
#Computer chose scissors
#Computer wins!
#
#Error: Bad input "lazer" to rpsls
#
