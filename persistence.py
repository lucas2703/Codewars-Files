def persistence(n):
    if n < 10:
        return 0
    
    n = str(n)
    count = 0
    temp_sum = 1
    while True:
        for x in range(len(n)):
            temp_sum *= int(n[x])
        count += 1
        n = str(temp_sum)
        temp_sum = 1
        if int(n) < 10:
            return count