def fact (num):     
    if num < 2 and num >= 0:
        return 1 
    return num * fact (num -1)

flag = False 
while not flag :
    num = int (input ("enter a number: "))
    if num < 0 :
        flag = True 
        print ("factorial of negative number is not possible")
    else : 
        print (f"the factrial of {num} is {fact (num)}")
