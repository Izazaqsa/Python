# class RationalNumbers :
#     def __init__(self,real , imaginary):
#         self.real_no =real 
#         self.imaginary_no = imaginary 

#     def __add__ (self, other):  # this is the function that gives extra fuctionality to the __add__ function (+)   no it is able to add the two objects of the class
#         return  (f"{self.real_no + other. real_no } + {self.imaginary_no + other.imaginary_no}i")
    
# num1 = RationalNumbers(10,8)
# num2 = RationalNumbers (12, 19)
# print (num1 + num2 )   # if you don't define the function add upper in the class then it will give an error becuase the sing (+) does not support the operand because 
                        # it only work on the numbers and the strings but these are the objects



class Person :
    def __init__(self, name , age ):
        self.name = name 
        self.age = age 

    def __gt__ (self, other):   # this function has change the functionality for the greater sign  (>) and with the 
        if self.age > other .age :   # help of this function now this (>) sign can compare the objects 
            return True 
        else : 
            return False

    
p1 = Person ('izaz', 22 )
p2 = Person ('yasir', 21)
if p1 > p2 :
    print (f"{p1.name} will pay the bill ")
else :
    print (f"{p2.name} will pay the bill ")