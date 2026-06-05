class Circle :
    pi = 3.14   # this attribute belongs to every object of the class 
    def __init__(self , radius): # while the attributes inside the init is specific to every object and every object will have it owns 
        self.radius = radius   # like the pi is common for  every cirle but the radius is specific for every circel 
        self.area = Circle.pi *radius *radius 

    def getarea (self ):
        return self.pi *self.radius *self.radius 
    
    def circumference (self):
        return 2 *self.pi* self.radius


rad = float (input ("enter the radius of the circle : "))   
circle01 = Circle(rad)
print (circle01.area)

# print (circle01. circumference ())
# print (circle01.pi)