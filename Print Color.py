# URL = http://www.codeskulptor.org/#user45_3G6Trw0ymr_0.py

# Register three buttons

###################################################
# Student should add code where relevant to the following.

import simplegui 


# Handlers for buttons
def set_red():
    global color
    color = "red"
    
def set_blue():
    global color
    color = "blue"
    
def print_color():
    print color

# Create frame
frame = simplegui.create_frame("Set and print colors", 200, 200)

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Print Color", 200, 200)
frame.add_button("Blue", set_blue)
frame.add_button("Red", set_red)
frame.add_button("Print", print_color)

# Start the frame animation
frame.start()


###################################################
# Test

set_red()
print_color()
set_blue()
print_color()
set_red()
set_blue()
print_color()

###################################################
# Expected output from test

#red
#blue
#blue
