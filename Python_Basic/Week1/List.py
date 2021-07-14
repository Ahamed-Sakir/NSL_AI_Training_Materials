num = 2
list1 = [num, 0, 'Ahamed']
list2 = [88, 7, list1, 4.5, 'Sakir']
print(list2[2][2])
print(list2[4])

# String is used as a list
str1 = 'Bangladesh'
print(str1[2])

# List concatenation
list1 = [1, 2, 3, 4]
print(list1 + [5, 6, 7, 8, 8])
print(1 in list1)

# List operation
new_list = [1, 5, 8]
new_list.append('sakir')
print(new_list)
new_list.insert(1, 'Ahamed')
print(new_list)
print((new_list.index('sakir')))
print(new_list.count('sakir'))
new_list1 = [55, 88, 1, 444]
print(max(new_list1))

# Range
my_number = list(range(5, 20))
print(my_number)
my_number = list(range(5, 20, 2))
print(my_number)


def frange(start, stop, step):
    i = start
    while i < stop:
        yield i
        i += step


for i in frange(.5, 1.0, .1):
    print(i)

# List slicing
my_list = [22, 12, 18, 50, 60, 65, 70, 80, 85]
print(my_list[4: 6])
print(my_list[6:])
print(my_list[:4])

list_jump = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_jump[2:9:2])
print(list_jump[3:-3])
print(list_jump[::-1])
print(max(list_jump))
print(min(list_jump))
print(sum(list_jump))

# List comprehension
my_list = [22, 12, 18, 50, 60, 65, 70, 80, 85]
new_list_auto = [num for num in my_list if num % 2 == 0]
print(new_list_auto)


# Matrix 2D to 1D using comprehension
matrix_2d = [[8, 2, 3],
            [6, 5, 6]]

matrix_1d = [number for row in matrix_2d for number in row]
print(matrix_1d)

# Another Example
vowels = 'aeiou'
sentence = 'I am awesome'
filtered_sentence = ''.join([letter for letter in sentence if letter not in vowels])
print(filtered_sentence)
