tuple1 = (45, 45, 45, 45)

for i in range(0,len(tuple1)):
    if tuple1[i]!= tuple1[0]:
        a= False
        print("Element of tuples are not identical in index:",i)
        exit()
    else:
        a=True

print(a)
'''
Author solution:

def check(t):
    return all(i == t[0] for i in t)

tuple1 = (45, 45, 45, 45)
print(check(tuple1))
'''