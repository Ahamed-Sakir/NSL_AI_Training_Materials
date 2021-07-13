# String to integer
str1 = "123456"
str1_to_int = int(str1)
print('This is an integer:', str1_to_int)

# Float to Integer
float_num = 6.2
float_to_int = int(float_num)
print(float_to_int)

# Integer to float
int_num = 6
int_to_float = float(int_num)
print('This is a float number:', int_to_float)

# Critical conversion between string_float_number to integer
string_value = '1245.256'
string_to_float = float(string_value)
float_to_int = int(string_to_float)
print('string float number conversion:', float_to_int)

"""N.B: int('1245.256') creates an error"""

# String conversion
num = 777
num_to_string = str(num)
print('This is string number:',num_to_string)

# Sometimes we need to str1 conversion in print function
num = 25
print('This is ' + str(num) + ' number')



