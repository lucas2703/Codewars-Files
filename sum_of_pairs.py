def sum_pairs(ints, s):
    
    _hash = set()
    
    for i in range(len(ints)):
        
        sumMinusElement = s - ints[i]
        
        if sumMinusElement in _hash:
            return [sumMinusElement, ints[i]]
        
        _hash.add(ints[i])
        
    return None