list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]
#list1[2][1][2].append(sub_list)
print("Before extension: ",list1)
for i in range(0,len(sub_list)):
    list1[2][1][2].append(sub_list[i])

print("After extension: ",list1)