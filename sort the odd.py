def sort_array(source_array):
    temp_odd = sorted([item for item in source_array if item % 2 != 0])
    odd_int = 0
    print(temp_odd)
    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:
            source_array[i] = temp_odd[odd_int]
            odd_int += 1
    return source_array

sort_array([5, 3, 2, 8, 1, 4])