class Father :
    def __init__(self, color , hair):
        print ('constructor from the father class ! ')
        self.father_eyes = color 
        self.hair_color = hair

    def voice (self):
        print ('i can sing  !! ')

class Mother : 
    def __init__(self,skin, beauty):
        print ('constructor from the mother class ')
        self.mother_skin = skin 
        self.mom_beauty = beauty 

    def cook (self):
        print ( 'i can cook in far better way ')

class Son (Father , Mother):
    def __init__(self, name,eyes_color, hair_clr, skin_clr, her_beauty,language):  # these are the parameters that every constructor needs 
        Father.__init__  (self,eyes_color , hair_clr)  # while creating an object only a single constructor is called but by mentioning like this all of the 
        Mother.__init__ (self,skin_clr, her_beauty)  #  mentioned constructor will be called 
        self.name = name 
        self.language = language 

    def play (self ):
        print ('i can play football ')

    def display (self):
        print (f"hi my name is {self.name} , my skin color is  {self.mother_skin} , my eyes looks {self.father_eyes}, and i am {self.mom_beauty} "  )

boy = Son ('ahmad ','black','black','white', 'ravishing','python')
boy.cook ()
boy.display ()
print(boy.mother_skin)
boy.voice ()