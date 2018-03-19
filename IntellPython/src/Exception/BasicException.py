name = 'I am an Array'
try:
    print(name[15])
except IndexError:
    print('IndexError has been found!')

print('This will be printed print.')