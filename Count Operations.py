# URL = http://www.codeskulptor.org/#user45_PqNwdwGS5t_2.py

# GUI with buttons to manipulate global variable count

###################################################
# Student should enter their code below

import simplegui
count = 0

# Define event handlers for four buttons

def reset():
    global count
    count = 0
    return count

def increment():
    global count
    count += 1
    return count

def decrement ():
    global count
    count = count - 1
    return count

def print_count():
    global count
    print count
    return count
    
# Create frame and assign callbacks to event handlers

frame = simplegui.create_frame("Count Operations", 200, 200)
frame.add_button("Reset", reset)
frame.add_button("Increment", increment)
frame.add_button("Decrement", decrement)
frame.add_button("Print", print_count)

# Start the frame animation
frame.start()
    
###################################################
# Test

# Note that the GLOBAL count is defined inside a function
reset()		
increment()
print_count()
increment()
print_count()
reset()
decrement()
decrement()
print_count()

####################################################
# Expected output from test

#1
#2
#-2
