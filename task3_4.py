#Exercise 4: Concatenate two lists in the following order
#list1 = ["Hello ", "take "]
#list2 = ["Dear", "Sir"]

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

result = [x + y for x in list1 for y in list2]
print(result) 
