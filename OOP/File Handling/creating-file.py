# file1= open ('info.txt','x')  # this will create a file 

# file1 = open ('info.txt','w')     # this will write into a file also create a file if doesn't exist 
# file1.write ('hi \nthis is Aizaz your friend \nhow are you ') 

# file1 = open('info.txt','r')  # use to read from the file can write in it and the file pointer will be at the start
# print (file1.read())

# file1 = open ('info.txt','r+')   # this provide to read and also write into the file while the file will be not override 
# print (file1.read())             # if you write first and then read then it will override , so basically it is used for the modificatoin of the file 
# file1.write('\ni am learning python from jenny mam')

# file2 = open ('data.txt', 'w+')   # used to write and read from the file but it will override the previous content of the file 
# file2.write ('hey this is aizaz your colleague')
# print(file2.read())   # if you try to read it so it won't display anything because the file pointer is at the end of the file 
# print(file2.tell ())  # tell the position of the file pointer 
# file2.seek (0)  # the seek () function is used to move the file pointer 
# print (file2.read ())    # now this will read the file because of the pointer at the start of the file 


file2= open ('data.txt','a+')  # use to append and read , can also creat a new file if doesn't exist 
file2 .write ('\nits a nice meeting with you i glad to meet with you , looking forward to meet again')
# information = file2.read()
# print (information)   # same it wont print anything because of the pointer at the end of the file 
file2.seek (0)
print (file2.read())