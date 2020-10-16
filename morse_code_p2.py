morse_code_dict =  {'.-...' : '&', '--..--' : ',', '....-': '4', '.....': '5',
     '...---...': 'SOS', '-...': 'B', '-..-': 'X', '.-.': 'R',
     '.--': 'W', '..---': '2', '.-': 'A', '..': 'I', '..-.': 'F',
     '.': 'E', '.-..': 'L', '...': 'S', '..-': 'U', '..--..': '?',
     '.----': '1', '-.-': 'K', '-..': 'D', '-....': '6', '-...-': '=',
     '---': 'O', '.--.': 'P', '.-.-.-': '.', '--': 'M', '-.': 'N',
     '....': 'H', '.----.': "'", '...-': 'V', '--...': '7', '-.-.-.': ';',
     '-....-': '-', '..--.-': '_', '-.--.-': ')', '-.-.--': '!', '--.': 'G',
     '--.-': 'Q', '--..': 'Z', '-..-.': '/', '.-.-.': '+', '-.-.': 'C', '---...': ':',
     '-.--': 'Y', '-': 'T', '.--.-.': '@', '...-..-': '$', '.---': 'J', '-----': '0',
     '----.': '9', '.-..-.': '"', '-.--.': '(', '---..': '8', '...--': '3', '   ' : ' ', '' : ' '
     }

def decode_bits(bits):
    # ToDo: Accept 0's and 1's, return dots, dashes and spaces
    bit = bits.strip('0')
    unit = 10000
    count = 1
    for i in range(1, len(bit)):
        if bit[i] == bit[i-1]:
            count += 1
        else:
            if count < unit:
                unit = count
                count = 1
            else:
                count = 1
    morse_code = ''
    for each in bit.split('0'*unit*7):
        for each1 in each.split('0'*unit*3):
            for each2 in each1.split('0'*unit):
                if each2 == '1'*unit:
                    morse_code += '.'
                elif each2 == '1'*unit*3:
                    morse_code += '-'
                else:
                    morse_code += '.'
            morse_code += ' '
        morse_code += '   '
    return morse_code
    

def decode_morse(morseCode):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    morseCode = morseCode.split(' ')
    _result = ""
    for x in morseCode:
        _result += morse_code_dict[x]
    _result = ' '.join(_result.split())
    return _result