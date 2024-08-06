s1=input("enter the string")
s2=input("Enter the second string")
len1= len(s1)
len2=len(s2)

if len1%2!=0 and len2%2!=0:
    s3= s1[0]+s2[0]+s1[int((len1-1)/2)]+s2[int((len2-1)/2)]+s1[len(s1)-1]+s2[len(s2)-1]
    print(s3)
else:
   print("both strings should be odd")