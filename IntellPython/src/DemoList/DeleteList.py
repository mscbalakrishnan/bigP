#an empty list
empty_list=[]

#a list of strings
str_list=['this', 'is', 'a', 'list']

#to remove a specific element, like 'is'
str_list.remove('is')
print(str_list)

#to remove an item of a specific index like 2
del str_list[2]
print(str_list)

#there are yet another way to remove an item of a specific index
str_list.pop(0)
print(str_list)