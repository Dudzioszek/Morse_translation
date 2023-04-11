morse_code_dict = { # uses latin alphabet and numbers 
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..', 
    'E': '.', 
    'F': '..-.', 
    'G': '--.', 
    'H': '....',
    'I': '..', 
    'J': '.---', 
    'K': '-.-', 
    'L': '.-..', 
    'M': '--', 
    'N': '-.', 
    'O': '---', 
    'P': '.--.',
    'Q': '--.-', 
    'R': '.-.', 
    'S': '...', 
    'T': '-', 
    'U': '..-', 
    'V': '...-', 
    'W': '.--', 
    'X': '-..-',
    'Y': '-.--', 
    'Z': '--..', 
    '0': '-----', 
    '1': '.----', 
    '2': '..---', 
    '3': '...--', 
    '4': '....-',
    '5': '.....', 
    '6': '-....', 
    '7': '--...', 
    '8': '---..', 
    '9': '----.'
}

def string_to_morse_code(text):
    morse_code = ''
    for char in text.upper():
        if char != ' ':
             # replaces letter with letter sample by dictionary
            morse_code += morse_code_dict[char] + ' ' 
        else:
            morse_code += ' '
    return morse_code

text = input("Enter text to translate to Morse code: ")
print(string_to_morse_code(text))