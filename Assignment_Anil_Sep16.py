#1.Define a variable as Integer(1) ,Float(1.0) and String(‘1’) and print and return the value and type of variable.

# A=1
# B='2'
# C=2.0
# print(A)
# print(type(C))



# 2.Redeclare the same variable as another number.(2,2.0 and ‘2’) and share your observation on result.
# A=2
# print(A)
# A="2.0"
# print(A)
##Observation = We can redeclare a variable simply by assigning new value (value type)


#3. Assigning a single value to several variables simultaneously with “=” operators.(a=b=c=10) and print the values of a,b and c..
# A=B=C = 10
# print (A)
# print (B)
# print (C)


#4.  Assign two variables a and b as integer and print the sum of a+b.
# a=5
# b=7
# Sum=(a+b)
# print (Sum)


# 5 . Write a Python program to create a list with five different fruits. eg:fruits = ["apple", "banana", "cherry", "date", "elderberry"]?
# fruits_list = ["apple", "banana", "cherry", "date", "elderberry"]
# 6. How do you access the second and fourth elements from the list.
# print (fruits_list[1])
# print (fruits_list[3])



#7.Modify the third element in the list numbers = [10, 20, 30, 40, 50] to 35.
# my_list =[10, 20, 30, 40, 50]
# print(my_list)
# my_list[2]=35
# print(my_list)


#8 . Create a Tuple:How do you create a tuple with the following elements: "red", "green", "blue"?
# tupple_elements = ("red", "green", "blue")
# print (tupple_elements)

#9 . Access Elements in a Tuple:How do you access the first and last elements in the tuple colors = ("red", "green", "blue", "yellow")?
# tuple_colors = ("red", "green", "blue", "yellow")
# print(tuple_colors)
# first_elements =tuple_colors[0]
# print(first_elements)
# last_elements=tuple_colors[-1]
# print(last_elements)

#10 . What happens if you try to change the second element of the tuple colors = ("red", "green", "blue")?
# tuple_colors = ("red", "green", "blue")
# tuple_colors[1]="Magenta"
# print (tuple_colors)

#ERROR : TypeError: 'tuple' object does not support item assignment


#11 .Tuple Unpacking: Given the tuple coordinates = (10, 20, 30), write a Python program to unpack it into three variables x, y, and z.
# tuple_coordinates = (10, 20, 30)
# x,y,z = tuple_coordinates
# print ("x=",x ,"y=",y,"z=",z)


#12 . Check Element in Tuple:Write a Python program to check if the element "blue" is present in the tuple colors = ("red", "green", "blue").
# tuple_colors = ("red", "green", "blue")
# if 'blue' in tuple_colors:
#     print ("blue is present in tuple_colors")
# else:
#     print("blue is not present in tuple_colors")


#13.  Tuple Length:Write a Python program to find the length of the tuple days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday").
# tuple_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
# print (tuple_days)
# print (len(tuple_days))


#14 .Create a Dictionary:Create a dictionary where the keys are student names and the values are their grades

# student_names_grades = {
#     "Alice" : 85,
#     "Bob" : 90,
#     "Charlie" : 78
# }
# print (student_names_grades)
#
# #15. Access Dictionary Values:How do you access Bob's grade from the dictionary students = {"Alice": 85, "Bob": 90, "Charlie": 78}?
# # Access Bob's grade
# bobs_grade = student_names_grades["Bob"]
# print("Bob's grade is",bobs_grade)

# 16 #Add a new student "David": 92 to the dictionary students = {"Alice": 85, "Bob": 90, "Charlie": 78} and remove "Charlie" from the dictionary.
# student_names_grades["David"]=92
# print (student_names_grades)
# #remove "Charlie" from the dictionary
# del student_names_grades["Charlie"]
# #print the new Dictionary values
# print (student_names_grades)
# #update Bob's grade to 95 in the dictionary
# student_names_grades ["Bob"] =95
# #print the new Dictionary values
# print (student_names_grades)

#17  #check if "Alice" is a key in the dictionary
# if "Alice" in student_names_grades:
#     print ("Alice is a Key in student_names_grades")
# else:
#     print ("Alice is not a Key in student_names_grades")


#18  # to find the number of key-value pairs in the dictionary
# number_pairs=len(student_names_grades)
#
# #print the Result
# print("The number of key value pairs in the dictionary is", number_pairs)




