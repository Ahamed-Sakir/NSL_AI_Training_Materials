# If condition
x = 5
y = 8
if x < y:
    print('Condition is true')

# if-else condition
if x > y:
    print('Condition is true')
else:
    print('Condition is false')

# elif
x = 9
y = 9
if x > y:
    print('x is greater than y')
elif x == y:
    print('x is equal to y')
else:
    print('x is smaller than y')

"""How to execute conditional statement with minimal code"""
x, y = 10, 8
result = 'x is greater than y' if (x > y) else 'x is smaller or equal to y'
print(result)

# Ternary operator
a = 50
b = 100 if (a <= 100 and a < 100) else 200
print(b)

# While loop
i = 1
while i < 10:
    print(i)
    i += 2

# For loop
x = [2, 5, 8, 44, 88]
print('xxx')
for i in x:
    print(i)

# List Comprehension
print([i**2 for i in x if i % 2 == 0])

# Dictionary Comprehension
dic = {k: k**2 for k in x}
print(dic)
