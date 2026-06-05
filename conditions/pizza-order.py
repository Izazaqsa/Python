print ("Hello to pizza core\n")
print ("place your order plz\n")
size = input("enter the size you want to order: ")
if (size == 'small'):
    print("the price is 500")
    price = 500 
elif (size == "medium"):
    print ("the price for the medium size is 700")
    price = 700 
elif(size == "large"):
    print ("the price for the large pizze is 100 ")
    price = 1000

pepperoni = input("do you want pepperoni? : ")
if (pepperoni =="yes"):
    if (size == "small"):
        print  ("the price of the pepperoni is 100 ")
        bill = price +100 
    else:
        print ("the pepperonin for medium and large pizze is 150")
        bill= price +150
else :
    print ("no addition to the bill")

cheese = input ("do you want an extra cheese : ")
if (cheese=="yes"):
    bill += 200 
    print (f"your total bill is {bill}")
else :
    print (f"your total bill is {bill}")

print ("thanks for choosing our pizz core")
