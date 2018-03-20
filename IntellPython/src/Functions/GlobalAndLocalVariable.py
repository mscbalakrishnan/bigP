x = "global"

def foo():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)
    
foo()

#Global and local variable with same name 
x = 5

def foo1():
    x = 10
    print("local x:", x)

foo1()
print("global x:", x)


###############
c = 1 # global variable
    
def add():
    c = c + 2 # increment c by 2
    print(c)

add()