test_case = int(input())
for i in range(0, test_case):
    a, b = input().split(' ')
    try:
        div = int(a) / int(b)
        print(int(div))
    except ZeroDivisionError:
        print('Error Code: integer division or modulo by zero')
    except ValueError as v:
        print('Error Code:', v)