def max_sequence(arr):
    current_sum = 0
    best_sum = 0
    for x in arr:
        current_sum = max(0, current_sum + x)
        best_sum = max(current_sum, best_sum)
    return best_sum