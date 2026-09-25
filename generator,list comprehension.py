#List Comprehension
#for
a = []
for x in range(1, 11):
    a.append(x)
print(a)                #1, 2, 3, 4, 5, 6, 7, 8, 9, 10

#create same list with comprehension
a = [x for x in range(1, 11)]
print(a)                            #1, 2, 3, 4, 5, 6, 7, 8, 9, 10

#for-if
a = []
for x in range(1,11):
    if x % 2 == 0:
        a.append(x) 
print(a)                  #2, 4, 6, 8, 10

#create same list with comprehension
a= [x for x in range(1, 11) if x % 2 == 0]
print(a)                                           #2, 4, 6, 8

#for-if-for-if 
a = []
for x in range(1,5):
    if x % 2 == 0:
        for y in range(1,4):
            if x + y == 5:
                a.append((x,y))
print(a)                            #[(2, 3), (4, 1)]

#create same list with comprehension
a = [(x,y) for x in range(1,5) if x % 2 == 0  for y in range(1,4) if x+y == 5]
print(a)                                          #[(2, 3), (4, 1)]

#set comprehension
l = [3,4,3,5,6,7,6]
   s = {x for x in l}
print(s)
#create list, set, dict comrehension with above list

#function1
def numbers():
    return 1 
    return 2 
n = numbers()
print(n)               #1
print(type(n))         #<class 'int'>

#generators
def numbers():
    yield 1 
    yield 2 
    yield 3 
    yield 4 
n = numbers() 
print(n)              #<generator object>
print(type(n))        #<class 'generator'>
print(next(n))        #1
print(next(n))        #2
print(n.__next__())   #3
print(n.__next__())   #4
print(next(n))        # stop iteration

def evennumbers():
    for x in range(1, 10):
        if x % 2 == 0:
            yield x 
n = evennumbers()
print(next(n))
print(n.__next__())      
for x in n:
    print(x)       #2, 4, 6, 8

#write generator to generate odd numbers
#write generator to generate even numbers
#write generator to generate prime numbers