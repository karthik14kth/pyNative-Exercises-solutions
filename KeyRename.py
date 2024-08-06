sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

newdict={'location':'New york'}

sample_dict.pop('city')

sample_dict = sample_dict | newdict

print(sample_dict)