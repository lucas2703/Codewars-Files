exclude_arr = ["the","of","in","from","by","with","and", "or", "for", "to", "at", "a"]

def generate_bc(url, separator):
    sol_string = ""
    elements = url.split('/')
    for i in range(0, len(elements)):
        if 'https' in elements[i]:
            elements.remove(elements[i])
            elements.remove(elements[i])
        else:
            break
    print(elements)
    elements[0] = 'HOME'
    elements = [x.upper() for x in elements]
    for a in range(len(elements)):
        # account for dots
        if '.' in elements[a]:
            temp = elements[a].split('.')[0]
            elements[a] = temp
        # account for question marks
        if '?' in elements[a]:
            temp = elements[a].split('?')[0]
            elements[a] = temp
        # remove index
        if 'INDEX' in elements[a]:
            elements.remove(elements[a])
    if len(elements) == 1:
        return '<span class="active">' + elements[0] + '</span>'
    # for first element
    sol_string += '<a href="/">HOME</a>' + separator
    # second element
    if len(elements[1]) > 30:
        long_temp = elements[1].split('-')
        long_acronym = ""
        for i in range(len(long_temp)):
            if long_temp[i].lower() not in exclude_arr:
                long_acronym += long_temp[i][0]
        sol_string += '<a href="/' + elements[1].lower() + '/">' + long_acronym + '</a>' + separator
    else:
        sol_string += '<a href="/' + elements[1].lower() + '/">' + elements[1] + '</a>' + separator
    # fill middle
    for b in range(1, len(elements) - 2, +1):  
        sol_string += '<a href="/'
        while(elements[b]):  
            sol_string += elements[b].lower() + '/'
            b += 1
            if (b == len(elements) - 1):
                break
        # account for elements > 30 characters
        if len(elements[b]) >= 30:
            print("long")
        else:
            sol_string += '">' + elements[b - 1] + '</a>' + separator
    # for last element
    if '-' in elements[-1]:
        elements[-1] = elements[-1].replace('-', ' ')
    sol_string += '<span class="active">' + elements[-1] + '</span>'  
    return sol_string

print(generate_bc("www.agcpartners.co.uk", " '' "))