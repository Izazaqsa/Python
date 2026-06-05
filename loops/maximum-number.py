num = input ("enter the numbers : ")
numbers = num.split ()
# print (numbers)

count = 0 
for i in numbers :
    count = count + 1

for i in range (count):
    numbers [i]= int (numbers[i])

print (numbers)
print (f"the length of the number is : {count}")
maximum_number = numbers[0]

for i in numbers :
    if (i > maximum_number):
        maximum_number= i 
print (f"the maximum number in the above list is : {maximum_number}")