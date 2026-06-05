import random 
numbers = random.randint (1,5)  # this will return any numbers from 1 to 5 also 1 and 5 will be included 
#print (numbers)

num2 = random.randrange (1,5)  # this will return any random numbers between the 1 and 5 , but the 5 will no be included
#print (num2)

num3= random.random ()  # this will return the floating number between the 0.0 and the 1.0 
# print (num3)

num4 = random.uniform (1,4)  # this will return the float number between the  1 and the 4 
# print (num4)

num_list = [3,5,7,2,1,7,8]
num = random.choice (num_list)   # this will return any number form the list randomly  
# print (num)

random.shuffle (num_list )  # this will shuffle the mention list 
print(num_list)