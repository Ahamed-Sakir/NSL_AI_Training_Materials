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


# Mixed arguments
def mix_arg(a, *values, **dic):
    print(a)
    print(values)
    print(dic)


mix_arg(10, 12, 15, 11, aa=2, b=3)


# Interesting thing
def my_func(x, y):
    """
    Here we see that print function is not executed in my_func.
    Because If a function has a return statement then nothing will be executed after the return statement.
    """
    z = x + y
    return z
    print('Sorry, I\'m not printing')


print(my_func(4, 5))


# Assign a function into a variable
def var_func(text):
    return text + ' loves programming'


variable = var_func
print(variable('Sakir'))


# Using function as an argument
def fun1(text):
    return text + ' is my country'


def fun2(arg_fun, name):
    return 'Hey, ' + arg_fun(name)


print(fun2(fun1, 'Bangladesh'))
