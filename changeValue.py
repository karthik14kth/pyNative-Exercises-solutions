sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}
print("Before update:\n",sample_dict)
sample_dict['emp3']['salary']=8500
print("After update:\n",sample_dict)

##My answer
'''
newdict={'emp3': {'name': 'Brad', 'salary': 8500}}

sample_dict.update(newdict)

print(sample_dict)
'''