from TestModule import *
printForward(10)

print(100*'-')

import os,sys
cwd = os.getcwd()
print("cwd:%s"%cwd)

sys.path.append(os.path.join(cwd,".."))
from Functions.BasicFunc import *
absolute_value(100)