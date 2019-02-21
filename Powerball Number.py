# URL = http://www.codeskulptor.org/#user45_txWpR453C9_1.py

# Compute and print powerball numbers.

###################################################
# Powerball function
# Student should enter function on the next lines.
import random
def powerball():
    number_1=random.randrange(1, 60)
    number_2=random.randrange(1, 60)
    number_3=random.randrange(1, 60)
    number_4=random.randrange(1, 60)
    number_5=random.randrange(1, 60)
    number_6=random.randrange(1, 60)
    number=random.randrange(1, 36)
    print "Todays numbers are "+str(number_1)+", "+str(number_2)+", "+str(number_3)+", "+str(number_4)+", "+str(number_5)+" and "+str(number_6)+". The Powerball number is "+str(number)+"."

    
###################################################
# Tests
# Student should not change this code.
    
powerball()
powerball()
powerball()
