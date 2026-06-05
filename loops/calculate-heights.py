heights = input ("enter the heights separated by a space : ")
height_list = heights.split ()
count = 0
for items in height_list :
    count = count +1
print (f"the list is contain of {count} heights")

# for i in height_list:
#     height_list[i]= int(height_list[i])   # thi i is the items of the list which is in str form not the indices of the list
#     print (height_list)                 so for this we count the items of list and then use the range function


for i in range (count):
    height_list[i]= int(height_list[i])    # this height_list[i] accessd the string at index 0 and the int (height_list[i])
    # convert that string into an int number and this way it is done for all of the elements of the list 
print (height_list)

total = 0 
for i in height_list:
    total = total + i
avg = total / count
print (f"the average height of the list is {avg:.0f}")      #:.of is used to round of the number to zero digit