#num = int (input("enter a number: "))
while True :
    num = int (input("enter a number: "))
    if num == 0 :
        break 
    print ("The table of the {num} is following : ")
    for i in range (1 , 11):
        multiple = num * i 
        print (f"{num} * {i} = {multiple}")