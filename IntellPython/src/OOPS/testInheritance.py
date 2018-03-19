class User:
    name = ""
 
    def __init__(self, name):
        self.name = name
 
    def printName(self):
        print ("Name  = " + self.name)
 
class Programmer(User):
    def __init__(self, name):
        self.name = name
 
    def doPython(self):
        print ("Programming Python")
 
brian = User("Rahul")
brian.printName()
 
diana = Programmer("Steve")
diana.printName()
diana.doPython()