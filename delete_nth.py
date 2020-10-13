def delete_nth(order,max_e):
    temp = []
    for x in order:
        if temp.count(x) < max_e:
            temp.append(x)
        
    return temp