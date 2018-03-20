#an empty list
empty_list=[]

#a list of strings
str_list=['this', 'is', 'a', 'list']

# add an element to the end of the list
str_list.append('appended')
print(str_list)

#insert an item at the defined index
str_list.insert(3,'inserted')
print(str_list)

#to get the index of the first matched item
print(str_list.index('a'))

#to count number of a specific element in a list
print(str_list.count('is'))

#to reverse the order of a list
str_list.reverse()
print(str_list)

#to sort the list in ascending order
str_list.sort()
print(str_list)

####Extend
odd = [1, 3, 5]

odd.append(7)

# Output: [1, 3, 5, 7]
print(odd)

odd.extend([9, 11, 13])

# Output: [1, 3, 5, 7, 9, 11, 13]
print(odd)