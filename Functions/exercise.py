# to calculate the numbers of can to paint a wall 
import math
cans = 0 
def calculate (height , width , coverage = 7):
    area = height* width 
    cans = area / coverage 
    print (f"the number of cans is {math.ceil(cans)}")    # ceil () round the number up to the nearest whole number

h = int (input ("enter the height : "))
w = int (input ("enter the width : "))
calculate(height = h, width= w)