a = 5 
b = 5
print (a is b )     # a and b pointing to the same location and (is) is checking the location so thats why it is
                    # returning the true value 
print (id (a))
print (id(b))

print (id(a)== id (b))
print(a is not b )