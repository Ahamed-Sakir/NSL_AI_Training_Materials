def search(value_list, key):
    index = None
    begin = 0
    end = len(value_list) - 1
    while begin <= end:
        mid = (begin + end) // 2
        if key == value_list[mid]:
            index = mid
            break
        # '''
        # If you want to return left most duplicate value
        # '''
        # if key == value_list[mid]:
        #     index = mid
        #     end = mid -1
        elif key > value_list[mid]:
            begin = mid + 1
        elif key < value_list[mid]:
            end = mid - 1
    return index


number_list = [1, 45, 78, 11, 11, 11, 98, 458, 6, 6, 6, 2]
sorted_list = sorted(number_list)

value = int(input('Input your searching value: '))
value_index = search(sorted_list, value)
print(f'Your value is in index: {value_index}')
# Lower bound
sorted_list.insert(value_index, value)
print(sorted_list)

