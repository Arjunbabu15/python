#Exercise 5: Display Fibonacci series up to 10 termsdef append_middle(s1, s2):

n1=0
n2=1

print("The fibonacci sequence: ")

for i in range(10):
print(n1, end=" ")

x = n1 + n2
n1 = n2
n2 = x
