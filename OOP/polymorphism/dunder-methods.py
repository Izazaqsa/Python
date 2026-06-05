class Author :
    def __init__(self,name , book , pages):
        self.name = name 
        self.book_name = book 
        self.pages = pages 
    
    def __str__(self):   # this is a dunder method and it is called automatically by printing the objec of the class 
        return (f"the book name is {self.book_name} , and the author of the book is {self.name} contains of a {self.pages}")

    
auth = Author ('izaz','deep work', 500)
print (auth)