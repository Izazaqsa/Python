class Instructor :
    followers = 0
    def __init__(self,name, address):
        self.name = name
        self.address = address
    def display (self, subject_name):
        print(f"hi my name is {self.name} and i teach {subject_name}")

    def update_followers(self,follower_name):
        self.followers += 1 


instructor1 = Instructor ('ali', 'mardan')
instructor1.display ('python')
print (f"i am from {instructor1.address}")
instructor1.update_followers('yasir')
print (f"{instructor1.followers}")