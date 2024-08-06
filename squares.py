numbers = [1, 2, 3, 4, 5, 6, 7]
square=[]
for i in range(0,len(numbers)):
    if (type(numbers[i])) == int:
        square.append(int(numbers[i])*int(numbers[i]))
    else:
        print("enter the list only with integers")

print(square)