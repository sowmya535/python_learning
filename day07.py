# =========================
# Set Methods
# =========================

# add
s = set()

s.add(1)
s.add(1.6)
s.add(2 + 3j)
s.add(True)
s.add(None)

# s.add([1, 2, 3])       # List cannot be added to a set
s.add((4, 5, 6))
# s.add({7, 8, 9})       # Set cannot be added to a set
# s.add({10: 'a', 11: 'b', 12: 'c'})  # Dictionary cannot be added

s.add('rakesh')
s.add(range(13, 16))

print(s)
# Output: {1, 1.6, (2+3j), None, (4, 5, 6), 'rakesh', range(13, 16)}
# Note: True is not added separately because True == 1


# =========================
# update
# =========================

s = set()

# s.update(1)             # int is not iterable
# s.update(1.6)           # float is not iterable
# s.update(2 + 3j)        # complex is not iterable
# s.update(True)          # bool is not iterable
# s.update(None)          # None is not iterable

s.update([1, 2, 3])
s.update((4, 5, 6))
s.update({7, 8, 9})
s.update({10: 'a', 11: 'b', 12: 'c'})
s.update('rakesh')
s.update(range(13, 16))

print(s)
# Output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
#          'r', 'a', 'k', 'e', 's', 'h', 13, 14, 15}


# =========================
# pop
# =========================

s = {1, 4, 3, 2, 5, 6, 7, 9}

print(s)
# Output: {1, 2, 3, 4, 5, 6, 7, 9}
# Order may vary

a = s.pop()
print(a, s)
# Output depends on set order
# Example: 1 {2, 3, 4, 5, 6, 7, 9}

b = s.pop()
print(b, s)
# Output depends on set order
# Example: 2 {3, 4, 5, 6, 7, 9}

# c = s.pop(3)             # TypeError: set.pop() takes no arguments
# print(c, s)


# =========================
# remove
# =========================

s = {4, 3, 2, 5, 8}

a = s.remove(8)
print(a, s)
# Output: None {2, 3, 4, 5}

# b = s.remove(9)          # KeyError: 9
# print(b, s)


# =========================
# discard
# =========================

s = {4, 3, 2, 5, 8}

a = s.discard(8)
print(a, s)
# Output: None {2, 3, 4, 5}

b = s.discard(9)
print(b, s)
# Output: None {2, 3, 4, 5}


# =========================
# clear
# =========================

s = {4, 3, 5, 2, 1}

a = s.clear()
print(a, s)
# Output: None set()


# =========================
# union, intersection, difference,
# symmetric_difference
# =========================

s = {1, 2, 3, 4}

l = [3, 4, 5, 6]
t = (3, 4, 5, 6)
s2 = {3, 4, 5, 6}
d = {3: 'c', 4: 'd', 5: 'e', 6: 'f'}
r = range(3, 7)
w = '3456'

print('Union:', s.union(l))
# Output: Union: {1, 2, 3, 4, 5, 6}

print('Intersection:', s.intersection(t))
# Output: Intersection: {3, 4}

print('Difference:', s.difference(s2))
# Output: Difference: {1, 2}

print('Symmetric Difference:', s.symmetric_difference(d))
# Output: Symmetric Difference: {1, 2, 5, 6}

print('Union:', s.union(w))
# Output: Union: {1, 2, 3, 4, '3', '4', '5', '6'}
# Note: numbers 3 and 4 are different from strings '3' and '4'

print('Union:', s.union(r))
# Output: Union: {1, 2, 3, 4, 5, 6}


# =========================
# Dict Methods
# =========================

d = {}

# d.update(5)             # TypeError
# d.update(5.4)           # TypeError
# d.update(4 + 5j)        # TypeError
# d.update(True)          # TypeError
# d.update(None)          # TypeError
# d.update([1, 2, 3])     # ValueError
# d.update((4, 5, 6))     # ValueError
# d.update({7, 8, 9})     # ValueError
# d.update('rak')         # ValueError
# d.update(range(10, 14)) # TypeError

d.update({10: 'j', 11: 'k', 12: 'l'})
print(d)
# Output: {10: 'j', 11: 'k', 12: 'l'}

d.update([
    [1, 'a'],
    (2, 'b'),
    'ab'
])

print(d)
# Output: {10: 'j', 11: 'k', 12: 'l', 1: 'a', 2: 'b', 'a': 'b'}

d.update(('ra', 'ke', 'sh'))
print(d)
# Output: {10: 'j', 11: 'k', 12: 'l', 1: 'a', 2: 'b',
#          'a': 'b', 'r': 'a', 'k': 'e', 's': 'h'}

d.update({
    (3, 'c'),
    (4, 'd')
})

print(d)
# Output: {10: 'j', 11: 'k', 12: 'l', 1: 'a', 2: 'b',
#          'a': 'b', 'r': 'a', 'k': 'e', 's': 'h',
#          3: 'c', 4: 'd'}


# =========================
# pop
# =========================

d = {3: 'c', 2: 'b', 1: 'a', 4: 'd'}

x = d.pop(2)
print(x)
# Output: b

# y = d.pop(100)           # KeyError: 100
# print(y)

z = d.pop(100, -1)
print(z)
# Output: -1


# =========================
# popitem
# =========================

d = {3: 'c', 2: 'b', 1: 'a', 4: 'd'}

x = d.popitem()
print(x, d)
# Output: (4, 'd') {3: 'c', 2: 'b', 1: 'a'}

y = d.popitem()
print(y, d)
# Output: (1, 'a') {3: 'c', 2: 'b'}


# =========================
# clear
# =========================

d = {3: 'c', 2: 'b', 1: 'a', 4: 'd'}

d.clear()
print(d)
# Output: {}


# =========================
# get
# =========================

d = {3: 'c', 2: 'b', 1: 'a', 4: 'd'}

x = d.get(2)
print(x, d)
# Output: b {3: 'c', 2: 'b', 1: 'a', 4: 'd'}

y = d.get(100)
print(y, d)
# Output: None {3: 'c', 2: 'b', 1: 'a', 4: 'd'}

z = d.get(100, -1)
print(z, d)
# Output: -1 {3: 'c', 2: 'b', 1: 'a', 4: 'd'}


# =========================
# setdefault
# =========================

d = {3: 'c', 2: 'b', 1: 'a', 4: 'd'}

x = d.setdefault(2)
print(x, d)
# Output: b {3: 'c', 2: 'b', 1: 'a', 4: 'd'}

y = d.setdefault(100)
print(y, d)
# Output: None {3: 'c', 2: 'b', 1: 'a', 4: 'd', 100: None}

z = d.setdefault(90, -1)
print(z, d)
# Output: -1 {3: 'c', 2: 'b', 1: 'a', 4: 'd', 100: None, 90: -1}

m = d.setdefault(90, -2)
print(m, d)
# Output: -1 {3: 'c', 2: 'b', 1: 'a', 4: 'd', 100: None, 90: -1}


# =========================
# keys, values, items
# =========================

d = {3: 'c', 2: 'b', 1: 'a', 4: 'd'}

dk = d.keys()
print(dk, type(dk))
# Output: dict_keys([3, 2, 1, 4]) <class 'dict_keys'>

dv = d.values()
print(dv, type(dv))
# Output: dict_values(['c', 'b', 'a', 'd']) <class 'dict_values'>

di = d.items()
print(di, type(di))
# Output: dict_items([(3, 'c'), (2, 'b'), (1, 'a'), (4, 'd')])
#         <class 'dict_items'>