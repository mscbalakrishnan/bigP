# Program to find the sum of all numbers stored in a list

# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# variable to store the sum
addVal = 0

# iterate over the list
for val in numbers:
    addVal = addVal+val
'''
# Output: The sum is 48
print("The sum is", addVal)

# Output: range(0, 10)
print(range(10))

# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(10)))

# Output: [2, 3, 4, 5, 6, 7]
print(list(range(2, 8)))

# Output: [2, 5, 8, 11, 14, 17]
print(list(range(2, 20, 3)))    '''
    
    
############for loop with else

digits = [0, 1, 5]

for i in digits:
    print(i)
else:
    print("No items left.")
    
    
# Example to illustrate
# the use of else statement
# with the while loop

counter = 0

while counter < 3:
    print("Inside loop")
    counter = counter + 1
else:
    print("Inside else")
    
    
    
# Use of break statement inside loop

for val in "string":
    if val == "i":
        break
    print(val)

print("The end")        


# Program to show the use of continue statement inside loops

for val in "string":
    if val == "i":
        continue
    print(val)

print("The end")


# pass is just a placeholder for
# functionality to be added later.
sequence = {'p', 'a', 's', 's'}
for val in sequence:
    pass