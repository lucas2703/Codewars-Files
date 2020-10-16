def remov_nb(n):
    answers = []
    # find sum of all 1-n 
    sum_temp = 0
    for i in range(n + 1):
        sum_temp += i
        
    # solve
    for a in range(n, 1,-1):
        if (sum_temp - a) % (a + 1) == 0:
            b = int((sum_temp - a) / (a + 1))
            if b < n:
                sum_except = sum_temp - a - b
                goal = a * b
                if sum_except == goal:
                    answers.append((b, a))
    
    return answers