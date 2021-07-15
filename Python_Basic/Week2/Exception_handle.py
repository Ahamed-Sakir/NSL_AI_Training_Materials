while True:
    try:
        number = int(input('Please enter a integer number:'))
    except ValueError:
        print('Oops! You have entered wrong types of number')
        break


try:
    value = 45 / 0
except:
    print('An error occurred')


try:
    str_1 = '10'
    print(str_1 + "hello")
    print(str_1 / 2)
except ZeroDivisionError:
    print("Divided by zero")
except (ValueError, TypeError):
    print("Type or value error occurred")
except:
    print('Oops! An error occurred')

# Using finally:
try:
    print(1)
    division = 45/0
except ZeroDivisionError:
    print('Oops! Please improve your math skill')
finally:
    print('Nobody can stop me')