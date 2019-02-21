# URL = http://www.codeskulptor.org/#user45_44Bshki1dC_0.py

# Compute the smaller root of a quadratic equation.

###################################################
# Smaller quadratic root formula
# Student should enter function on the next lines.
def smaller_root(a,b,c):
    discriminant = ((b**2)-(4*a*c))
    if discriminant > 0:
        solution_1=((-b+(discriminant**0.5))/(2*a))
        solution_2=((-b-(discriminant**0.5))/(2*a))
        if solution_1>solution_2:
            return solution_2
        else:
            return solution_1
    elif discriminant==0:
        solution_3=((-b)/(2*a))
        return solution_3
    else:
        return "Error: No real solutions"



###################################################
# Tests
# Student should not change this code.

def test(a, b, c):
    """Tests the smaller_root function."""
    
    print "The smaller root of " + str(a) + "x^2 + " + str(b) + "x + " + str(c) + " is:" 
    print str(smaller_root(a, b, c))
        

test(1, 2, 3)
test(2, 0, -10)
test(6, -3, 5)

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#The smaller root of 1x^2 + 2x + 3 is:
#Error: No real solutions
#None
#The smaller root of 2x^2 + 0x + -10 is:
#-2.2360679775
#The smaller root of 6x^2 + -3x + 5 is:
#Error: No real solutions
#None
