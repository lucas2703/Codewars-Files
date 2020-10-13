def narcissistic( value ):
    sum = 0
    for i in range(len(str(value))):
        temp_add = value // 10**i % 10
        temp_sum = temp_add ** len(str(value))
        sum += temp_sum
    if sum == value:
        return True
    else:
        return False