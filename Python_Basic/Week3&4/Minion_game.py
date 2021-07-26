def minion_game(string):
    str_len = len(string)
    stuart_value = 0
    kevin_value = 0
    for i in range(str_len):
        if string[i] in 'AEIOU':
            kevin_value += (str_len - i)
        else:
            stuart_value += (str_len - i)
    if kevin_value > stuart_value:
        print(f'Kevin {kevin_value}')
    elif kevin_value == stuart_value:
        print('Draw')
    else:
        print(f'Stuart {stuart_value}')



if __name__ == '__main__':
    s = input()
    minion_game(s)