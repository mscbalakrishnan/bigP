# class Error is derived from super class Exception
class Error(Exception):
 
    # Error is derived class for Exception, but
    # Base class for exceptions in this module
    pass
 
class TransitionError(Error):
 
    # Raised when an operation attempts a state 
    # transition that's not allowed.
    def __init__(self, prev, nex, msg):
        self.prev = prev
        self.next = nex
 
        # Error message thrown is saved in msg
        self.msg = msg
try:
    raise(TransitionError(2,3*2,"Not Allowed"))
 
# Value of Exception is stored in error
except TransitionError as error:
    print('Exception occured: ',error.msg)


# NetworkError has base RuntimeError
# and not Exception
class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg
 
try:
    raise Networkerror("Bad hostname")
 
except Networkerror as e:
    print (e.args)
