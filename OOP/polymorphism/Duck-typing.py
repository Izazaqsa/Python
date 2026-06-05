class Duck :
    def speaks (self):
        print ('quak quak')
    
    def swims (self):
        print ('i am duck and i can swims')

class Dog :
    def speaks (self ):
        print ('ghwab ghwab')
    
    def swims (self):
        print ("i am a dog and i can swims ")

class Person :
    def speaks (self):
        print ('i can talk')

def display (object):
    object.speaks ()
    object. swims()

duck = Duck ()    # so see for function dispaly it doesn't matter  theobject belongs to which function but it simply
display (duck)   # calls the methods if it belongs to  that object 
dog = Dog ()
display (dog)
person = Person()   # for person it won't work because for the object of the person the swims function is not define 
display  (person)   # so when it try to access it then it will show an error 