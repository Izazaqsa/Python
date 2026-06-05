class Human :
    eyes = 2
    def __init__(self,name, age):
        print ('from human class')
        self.name = name 
        self.age = age 

    def walk (self):
        print ('i can walk')

class Male (Human) :
    Gender ='male'
    def __init__(self,ad, H_name ,H_age):
        Human.__init__(self,H_name, H_age)
        print ('from male class')
        self.address = ad

    def work_hard(self):
        print ('i can work hard')

    def introduction (self):
        print (f'hi i am {self.name} , my age is {self.age} and i am from {self.address}')

class Female (Human):
    Gender ='Female'
    def __init__(self, number,F_name,F_age):
        super().__init__ (F_name,F_age)
        print ('from female class')
        self.number = number 

    def sing (self):
        print ('i can sing a song ')

female1 = Female(123,'amna',23)
print (female1.Gender)

male1= Male('dir','izaz',22)
print (male1.name)
male1.introduction()