f = open("test.txt",encoding = 'utf-8')
print(f.read())
print(f.read(4)) 
print(f.readline())
# perform file operations
f.close()