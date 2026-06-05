# import random
# name = input ("enter the names of the individual in the group : ")
# friends  = name.split (",")     # split is the function that split the string into a piece by the mention condition 
# #when it is matched , like if i enter the comma then it will split it and store it in list automatically
# print (friends)
# num = random.randint(1,5)
# if len(friends) > 5 :
#     print("you are out of range it only takes five friends names so plz stay between the range")
# else : 
#     if (num == 1):
#         print (friends[0])    
#     elif (num ==2 ):
#         print(friends[1])
#     elif (num == 3):
#         print (friends [2])
#     elif (num ==4):
#         print (friends[3])
#     else :
#         print(friends [4])

# this is the limited programm and it will not work if the range goes beyond from the 5 


import random 
names = input ("enter the names of the indiviual in the group : ")  
friends= names.split (",")  # split the names by commas and will store it in the list 
length = len(friends)   #return the length of the list 
choice = random.randint (0 , length-1)  # use to pic a random choice between the 0 and the length of the list 
print (f"{friends[choice]} will pay the bill " )   # will print the choosen name 
