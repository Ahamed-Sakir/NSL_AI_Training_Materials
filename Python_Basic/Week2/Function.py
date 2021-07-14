def func():
    print('You are calling me')


func()


# Function with argument
def func_double(x):
    return x * 2


return_value = func_double(6)
print(return_value)


# Multiple arguments
def total_sum(*values):
    sum = 0
    for num in values:
        sum += num

    return sum


print(total_sum(44, 6, 10, 70))


# Double **
def my_dic(**values):
    dic = values
    return dic


print(my_dic(a=1, b=2, c=3))
