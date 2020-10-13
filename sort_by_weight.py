def order_weight(strng):
    input_list = strng.split(' ')
    
    temp_weights = [add_digits(a) for a in input_list]
    
    weight_comparison = [x for _, x in sorted(zip(temp_weights, input_list))]
    
    return ' '.join(weight_comparison) 
    
def add_digits(num):
    temp_sum = 0
    for x in range(len(num)):
        temp_sum += int(num[x])
    return temp_sum
    