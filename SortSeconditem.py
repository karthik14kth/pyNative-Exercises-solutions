import operator

tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))

print(sorted(tuple1,key=operator.itemgetter(1)))

'''
Author solution:
tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
tuple1 = tuple(sorted(list(tuple1), key=lambda x: x[1]))
print(tuple1)
'''