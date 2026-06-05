class Human :
    def __init__(self,arms):
        self.ears = 2 
        self.nose = 1 
        self.no_arms = arms

    def talk (self):
        print ('hi')
    
    def work (self):
        print ('i can work ! ')

class Male (Human):
    def __init__(self,name,arms):
        super().__init__ (arms)   # the arms parameters is needed in the parent init function thats why it has to be passed here
        self.name = name

    def flirt (self):
        print ('i can flirt ')

    def work (self):   # override the work  function of the class of the parent class
        print ('i can code ')

    def talk (self):
        super ().talk ()   # this keep the parent class as it is and also modify it in derived class 
        print ('how are you ?')
    
    def display (self):
        print (f" i am {self.name}, i have {self.ears} ears , {self.no_arms} arms and {self.nose} nose")

izaz = Male ('izaz',2)
izaz.talk ()
# izaz.flirt ()
# print (izaz.ears )    # this ears of the parent cannot be accessed directly for this you have to use the super function
# print (izaz.no_arms)

izaz.display ()