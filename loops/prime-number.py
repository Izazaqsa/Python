print ("prime numbers between 1 and 100 ")

for num in range (2,100+1):
    for i in range (2 , num):
        if (num%i ==0):
            break 
    else : 
        print (f"{num} is prime number")
