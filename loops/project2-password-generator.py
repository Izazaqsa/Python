# import random 
# letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
#            'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# numbers = ['0','1','2','3','4','5','6','7','8','9']
# symbols = ['!','@','#','$','%','^','&','*','/','|','~']

# password = []

# print ("Welcome to the password Generator : ")
# characters = int (input ("how many letter you want to choose : "))
# num = int (input ("how many number you want to choose : "))
# sym = int (input("how many symbols  you want to choose : "))

# for i in range (1 , characters+1):
#     char = random.choice (letters)
#     password += char 

# for i in range (1,num+1):
#     numb = random.choice (numbers)
#     password += numb 

# for i in range (1 , sym + 1):
#     symb = random.choice (symbols)
#     password += symb 

# random.shuffle(password)
# # print (f"the password is  {password}")

# code = ""
# for i in password : 
#     code += i 

# print (f"the password is {code}")



# aother way 
import random 
import string 

letter = int (input ("enter the number of the letters : "))
numbers = int (input("enter the numbers you want to include in the password : "))
symbols = int (input("enter the numbers of the symbols : "))

password = []

for i in range (1, letter+1):
    char = random.choice (string.ascii_letters)
    password += char 

for i in range (1,numbers+1):
    num = random.choice (string.digits)
    password += num 

for i in range (1,symbols+1):
    symb = random.choice (string.punctuation)
    password += symb 

random.shuffle (password)
code = ""
for i in password : 
    code += i 

print (f"the password that is generated is : {code}")