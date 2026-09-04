# #append
# l = ['a', 'b', 'c']
# l.append(34)              #['a', 'b', 'c', 34]
# l.append(34.3)            #['a', 'b', 'c', 34, 34.3]
# l.append(4+3j)            #['a', 'b', 'c', 34, 34.3, (4+3j)]
# l.append(True)            #['a', 'b', 'c', 34, 34.3, (4+3j), True]
# l.append(None)            #['a', 'b', 'c', 34, 34.3, (4+3j), True, None]
# l.append([0,1,2])         #['a', 'b', 'c', 34, 34.3, (4+3j), True, None, [0, 1, 2]]
# l.append((3,4,5))         #['a', 'b', 'c', 34, 34.3, (4+3j), True, None, [0, 1, 2], (3,4,5)]
# l.append({6,7,8})          #['a', 'b', 'c', 34, 34.3, (4+3j), True, None, [0, 1, 2], (3,4,5), {6, 7, 8}]
# l.append({9:'a', 10:'b', 11:'c'})      #['a', 'b', 'c', 34, 34.3, (4+3j), True, None, [0, 1, 2], (3,4,5), {6, 7, 8}, {9: 'a', 10: 'b', 11: 'c'}]
# l.append('sowmya')            #['a', 'b', 'c', 34, 34.3, (4+3j), True, None, [0, 1, 2], (3,4,5), {6, 7, 8}, {9: 'a', 10: 'b', 11: 'c'}, 'sowmya']
# l.append(range(12,15))         #['a', 'b', 'c', 34, 34.3, (4+3j), True, None, [0, 1, 2], (3,4,5), {6, 7, 8}, {9: 'a', 10: 'b', 11: 'c'}, 'sowmya', range(12, 15)]
# print(l)


 # extend() 
#  l = ['a', 'b', 'c'] 
#  l.extend(34)                           #error 
#  l.extend(34.3)                         #error
#  l.extend(4+3j)                         #error
#  l.extend(True)                         #error
#  l.extend(None)                         #error
# l.extend([0,1,2])                      #['a', 'b', 'c', 0,1,2] 
# l.extend((3,4,5))                      #['a', 'b', 'c', 0,1,2, 3,4,5]
# l.extend({6,7,8})                      #['a', 'b', 'c', 0,1,2, 3,4,5, 6,7,8]
# l.extend({9:'a', 10:'b', 11:'c'})      #['a', 'b', 'c', 0,1,2, 3,4,5, 6,7,8, 9, 10, 11]
# l.extend('sowmya')                      #['a', 'b', 'c', 0,1,2, 3,4,5, 6,7,8, 9, 10, 11, 's', 'o','w', 'm', 'y','a']
# l.extend(range(12,15))                    #['a', 'b', 'c', 0,1,2, 3,4,5, 6,7,8, 9, 10, 11, 's', 'o','w', 'm', 'y','a',12, 13, 14]
# print(l)



# insert()
#positive index 
# l = ['a', 'b', 'c', 'd']
# l.insert(2, 'hi')               
# print(l)                   #['a', 'b', '2', 'c', 'd']
# l.insert(10, 'hi')
# print(l)                   #error
#  #negative index
# l = ['a', 'b', 'c', 'd', 'e'] 
# l.insert(-2, 'hi')  
# print(l)                   #['a', 'b', 'c','hi','d', 'e'] 
# l.insert(-100, 'hi') 
# print(l)                  ##[ 'hi', 'a', 'b', 'c','d','hi', 'e']
    

    #pop()
     l = [1, 2, 3, 4, 5] 
     a = l.pop() 
     print(a, l) 
     b = l.pop(2)
      print(b, l) 
      # c = l.pop(7)
       del l[0] 
       print(l)