arr = [10, 20, 30, 40, 50]
print(arr[0])
print(arr[1])
print(arr[2])

#negative indexing
arr = [10, 20, 30, 40, 50]
print(arr[-1])
print(arr[-2])

#Adding an element in an array using append()
add = ['a', 'b', 'c']
add.append('d')
print(add)

#Removing elements of an array using del, remove() and pop()
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
del colors[4]
colors.remove("blue")
colors.pop(3)
print(colors)

#insert
arr = [1,2,3,4,5,6,7]

arr.insert(3,10)
print(arr)

#Modifying elements of an array using Indexing 
fruits = ["Apple", "Banana", "Mango", "Grapes", "Orange"]
fruits[1] = "Pineapple"
fruits[-1] = "Guava"
print(fruits)

#different data types
student_marks = ['Akkas' , 45, 36.5]
marks = student_marks[1]+student_marks[2]
print(student_marks[0] + ' has got in total = %d + %f = %f ' % (student_marks[1], student_marks[2], marks ))

