# None
def my_func(x=None):
    if x:
        return x * x
    else:
        return 0


print(my_func(0))
print(my_func(5))

# Dictionary
my_dict = {'one': 2, 'two': 4, 'three': 6}
print(my_dict['one'])
my_dict['two'] = 9
print(my_dict)
my_dict[2] = 25
print(my_dict)
print(2 in my_dict)
print('2' in my_dict)
print('six' not in my_dict)

print(my_dict.get(5, 'There is no key like this'))

# Dictionary comprehension
list_key = [1, 2, 3]
list_value = ['sakir', 'Anannya', 'VU']
new_dic = {list_key[i]: list_value[i] for i in range(len(list_key))}
print(new_dic)

# Tuples
tuple_1 = ('first', 'second', 'third')
print(tuple_1[2])
a, b, c = tuple_1
print(b)
number = (1, 2, 5, 8, 9, 11, 45, 78, 11, 9)
a, *b, c = number
print(a)
print(b)
print(c)