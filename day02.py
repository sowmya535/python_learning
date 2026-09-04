# print all keywords in python

import keyword
print("Python Keywords:")
print(keyword.kwlist)


# print how many keywords are in python
print("Number of keywords:", len(keyword.kwlist))


# create variables for age and name
age=22
name="sowmya"
print("Age:", age)
print("Name:", name)

# create variable with special symbol
#  special symbols cannot be used directly in variable names
# example: my-name = "sowmya" - invalid
# but underscore(_)is allowed:
my_name = "sowmya"
print("My name:", my_name)


# create variable starting with a number
# variable names cannot start with a number
# ex: 1name = "sowmya" - invalid

#correct way:
name1 = "sowmya"
print("Name:", name1)


# assign multiple variables to a single value
x = y = z = 100

print("x =", x)
print("y =", y)
print("z =", z)


# assign a variable to a value and re-assign it
number = 10
print("Before re-assignment:", number)

number = 50
print("After re-assignment:", number)


# swap variables in different ways
# method 1: using temporary variable
a = 10
b = 20

temp = a
a = b
b = temp

print("After swap using temp:")
print("a =", a)
print("b =", b)


# method 2: without using a temporary variable
a = 10
b = 20
a, b = b, a
print("After swap without temp:")
print("a =", a)
print("b =", b)

# method 3: using arthematic operators
a = 10
b = 20
a = a + b
b = a - b
a = a - b

print("After arithematic swap:")
print("a =", a)
print("b =", b)


# create and delete a variable
student = "sowmya"
print("Before deleting:", student)
del student
# student cannot be used after this because it is deleted
print("Variable 'student' has been deleted")

# write a single-line comment
print("Hello Python")

# write a multi-line comment
"""
This is multi-line comment.
It can contain multiple lines.
It is useful for writing.
long explanations.
"""
print("Multi-line comment completed")



