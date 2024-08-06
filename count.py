str =input("enter the string")
character=0
number=0
symbols =0
for i in range(0,len(str)):
    if str[i].isalpha():
        character+=1
    elif str[i].isnumeric():
        number+=1
    elif str[i].isalnum()== False and  str[i].isspace()== False:
        symbols+=1
print("character:",character,"\nDigit:",number, "\nsymbol:",symbols)
