#Exercise 4: Delete a list of keys from a dictionary
#Given:
#sample_dict = {
#"name": "Kelly",
#"age": 25,
#"salary": 8000,
#"city": "New york"
#}
# Keys to remove
#keys = ["name", "salary"]

#answer

sample_dict = {
"name": "Kelly",
"age": 25,
"salary": 8000,
"city": "New york"
}
keys = ["name", "salary"]

for k in keys:
sample_dict.pop(k)
print(sample_dict)
