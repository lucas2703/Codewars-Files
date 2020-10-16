def rot13(message):
    print(message)
    
    capital_indices = get_indices(message)
    message = message.lower()
    
    new_message = ""
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', ' ', '!', '+', '.']
        
    # magic happens here mainly
    for i in range(len(message)):
        if message[i].isdigit():
            new_message += message[i]
            continue
        temp_pos = alphabet.index(message[i])
        if temp_pos == 26:
            new_message += ' '
        elif temp_pos == 27:
            new_message += '!'
        elif temp_pos == 28:
            new_message += '+'
        elif temp_pos == 29:
            new_message += '.'
        elif temp_pos + 13 >= 26:
            temp = 26 - alphabet.index(message[i])
            new_message += alphabet[13 - temp]
        else:
            new_message += alphabet[temp_pos + 13]
    
    if len(capital_indices) > 0:
        for i in range(len(capital_indices)):
            new_message = new_message.replace(new_message[capital_indices[i]], new_message[capital_indices[i]].upper(), 1)
    
    return new_message

def get_indices(s):
    return [i for i, c in enumerate(s) if c.isupper()]