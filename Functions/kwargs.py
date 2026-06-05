def info (**information):   # the double star convert the arguments into dictionary as the key and its values 
    print (information)
    for i , j in information.items ():    # used to access the items of the dictionary , the  i will store the key and the j will store the value
        print (f"{i}  : {j}")

info (name = "aizaz", age = 21 , dept= "cs" , address= "akhagram")