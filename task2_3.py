#Exercise 3: Arrange string characters such that lowercase letters should come first

str1 = "ARjuNbABu"
print('Original String:', str1)
lower = []
upper = []
for char in str1:
if char.islower():
lower.append(char)
else:
upper.append(char)

sorted_str = ''.join(lower + upper)
print('Result:', sorted_str)
