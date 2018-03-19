# Function to take multiple arguments
def add(datatype, *args):

    # if datatype is int
    # initialize answer as 0
    if datatype =='int':
        answer = 0
        
    # if datatype is str
    # initialize answer as ''
    if datatype =='str':
        answer =''

    # Traverse through the arguments
    for x in args:

        # This will do addition if the 
        # arguments are int. Or concatenation 
        # if the arguments are str
        answer = answer + x

    print(answer)

# Integer
add('int', 5, 6)

# String
add('str', 'Hi ', 'Geeks')

class Human:
 
    def sayHello(self, name=None):
 
        if name is not None:
            print ('Hello ' + name)
        else:
            print ('Hello ')
 
# Create instance
obj = Human()
 
# Call the method
obj.sayHello()
 
# Call the method with a parameter
obj.sayHello('Guido')