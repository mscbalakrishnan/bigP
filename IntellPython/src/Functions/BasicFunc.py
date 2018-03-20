def absolute_value(num):
    """This function returns the absolute
    value of the entered number"""
    if num >= 0:
        return num
    else:
        return -num
# Output: 2
print(absolute_value(2))
# Output: 4
print(absolute_value(-4))

#arbitary arguements
def greet(*names):
    """This function greets all
   the person in the names tuple."""

# names is a tuple with arguments
    for name in names:
        print("Hello",name)

greet("Monica","Luke","Steve","John")

def varFunc(name,*args):
        print("This is the first argument "+str(name))
        #This print will make you understand that the args is a list
        print(args)
        for item in args:
                print(item)

print("First time:")
varFunc("of 1st function call",2, 3, 4, 5)

print("Second time:")
varFunc("of 2nd function call","asd","Bcd")

print("Third time:")
varFunc("and only argument of 3rd function call")  