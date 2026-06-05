import random 
options = ["rock","paper","scissor"]
print(f" 0 for Rock \n 1 for the Paper \n 2 for the scissor")
user_choice = int (input("enter your choice : "))
system_choice = random.randint (0,2)
if user_choice not in [0,1,2]:
    print ("invalid options ")
else :
    print (f"\nuser chioce {options[user_choice]} \nsystem choice {options[system_choice]} \n")
    if (user_choice==system_choice):
        print("Draw")
    elif (user_choice==0 and system_choice==1):
        print ("System wins")
    elif (user_choice==0 and system_choice==2):
        print("User wins")
    elif (user_choice==1 and system_choice==0):
        print ("User wins ")
    elif (user_choice==1 and system_choice==2):
        print ("System wins")
    elif (user_choice==2 and system_choice==0):
        print("System wins")
    elif (user_choice==2 and system_choice==1):
        print("User wins")

print ("thanks for playing")