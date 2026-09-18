def add(a, b):
    print('add function')
    c = a + b 
    return c 
    pirnt('HI')
def sub(a, b):
    print('sub function')
    c = a - b
    return 
def div(a, b):
    print('div function')
    c = a / b 
x = add(10, 15)   #add function
y = sub(20, 10)   #sub function
z = div(25, 10)   #div function
print(x)         #25
print(y)         #None
print(z)         #None
print()

#Type of arguments
def detail(name, age, rollno):
    print(f'My name is {name}')   #My name is rakesh
    print(f'My age is {age}')     #My age is 20
    print(f'My rollno is {rollno}')   #My rollno is A101

#positional 
detail('rakesh', 20, 'A101')    #My name is rakesh, #My age is 20, #my rollno is A101
detail(20, 'A101', 'rakesh')    #My name is 20, #My age is A101, #My rollno is rakesh

#keyword
detail(age=20, rollno='A101', name='rakesh') #My name is rakesh, #My age is 20, #My rollno is A101
detail(rollno='A101', age=20, name='rakesh')  #My name is rakesh, #My age is 20, #My rollno is A101

#default
def add(a, b=10, c=20):
    return a + b + c 
print(add(1))          #31
print(add(1,2))        #23
print(add(1,2,3))       #6

#order of = in function def. Default Arguments after Non default arguments
def sub(a=10, b, c):
    pass 

#order of = in function call. Keyword Arguments after Positional Arguments
add(a=10, b, c)

def f1(*a):
    print(a)         #(1,2,3,4)
    print(type(a))   #<class 'tuple'>
f1(1,2,3,4)

def f2(**a):
    print(a)
    print(type(a))
f2(1,2,3,4)             # **a only accepts keyword arguments not positional arguments
f2(a=1, b=2, c=3, d=4)   #{'a'=1, 'b'=2, 'c'=3, 'd'=4}, <class 'dict'>