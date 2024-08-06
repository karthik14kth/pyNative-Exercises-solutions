sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]

for i in range(0,len(keys)):
    sample_dict.pop(keys[i])

new_dict=dict(reversed(sample_dict.items()))

print(new_dict)