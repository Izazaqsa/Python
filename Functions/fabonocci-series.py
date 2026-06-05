
def fab (n):
    if n < 2 :
        return n 
    return fab (n-1)+ fab (n-2)

flag = False 
while not flag : 
    num = int (input ("enter a number: "))
    if num < 0 : 
        print ("exiting ... negative number is entered ")
        flag = True 
    else :
        print (f"fab number on the position {num} is {fab(num)}")



# in loop way 
# n = int (input("enter a number : "))
# def fab (n):
#     num , num2 = 0 , 1 
#     for _ in range (n):      # the underscore does not care about the loop values , _ skip the values and just repeat the loop 
#         num , num2 = num2 , num + num2 
#     return num

# print (f"the fabnoccin number on the position {n} is {fab(n)}")