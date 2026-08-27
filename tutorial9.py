#List - Items or Elements (Mutable- It can change and It ordered) Data Structure(List) Tuple,
# students_list = ["Awele", "Jennifer"]
# student = "Precious"
# students_list.append(student)
# students_list.insert(1, student)
# print(students_list)
# name = "VICTOR"
# name = name.lower()
# print(name)
# students= ["Tope", "Shola", "Bola", "Shola"]
# age= [20, 40,11, 27, 90, 13]
# age.sort(reverse=True)
# print(age)
# science_students = ["Awele", "Jennifer", "Victor"]
# students.extend(science_students)
# students.remove("Shola")
# students.pop(2)
# del students
# students.clear()
# students.sort(reverse=True)
# print(students)
# #Sort is case sensitive
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort()
# thislist.sort(key=str.lower)
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)

# original_list = ["Awele", "Jennifer", "precious", "Victor"]
# # new_list = original_list # Bad way of copying a list
# print(original_list)
# new_list = original_list.copy() # Good way of copying a list
# another_new_list = list(original_list) #Good way of copying a list
# another_new_list_two = original_list[:]

# new_list.reverse()
# print(new_list)

#Tuple - Immumatable
# thistuple = ("apple", "banana", "cherry")
# thistuple_two = "apple", "banana", "cherry"
# print(thistuple[0])
# print(thistuple_two[1])
# print(len(thistuple_two))

# new_tuple = ("apple",)
# print(type(new_tuple))

# thistuple = ()
# print(type(thistuple))
#
# my_tuple = tuple(("Orange", "Banana", "Mango"))
# print(type(my_tuple))

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(type(thistuple))
# # In order to update a tuple we need to first convert it to a list we then perform the modification and convert back to a tuple
# new_list = list(thistuple)
# new_list.pop()
# print(new_list)
# new_tuple = tuple(new_list)
# del new_tuple
# print(new_tuple)

# fruits = ("apple", "banana", "cherry")
# (red, yellow, pink) = fruits
# print(red)
# print(yellow)
# print(pink)
# (red, *yellow) = fruits
# print(red)
# print(yellow)

# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
#
# (green, *tropic, blue, red) = fruits
#
# print(green)
# print(tropic)
# print(blue)
# print(red)

# fruits = ("apple", "banana", "cherry", "apple")
# # mytuple = fruits * 3
#
# print(fruits.index("apple"))






