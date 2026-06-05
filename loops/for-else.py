tuple1 = (3,5,2,7,-3,9)
for num in tuple1 :
    print (num)
    if num == -3:   # this will forcefully break the loop and the else block will not be executed 
        break
else:
    print ("successfully completed")