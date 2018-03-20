#Traversing
arrayElement = ["One", 2, 'Three' ]
for i in range(len(arrayElement)):
    print(arrayElement[i])
    
arrayElement2D = [ ["Four", 5, 'Six' ] , [ 'Good',  'Food' , 'Wood'] ]
for i in range(len(arrayElement2D)):
    print(arrayElement2D[i])

for i in range(len(arrayElement2D)):
    for j in range(len(arrayElement2D[i])):
        print(arrayElement2D[i][j])    
        


