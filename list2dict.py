keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dictionary={}

if len(keys)== len(values):
    for i in range(0,len(keys)):
            dictionary[keys[i]]= values[i]
else:
    print("Both the list index should be equal")
    exit()

print(dictionary)