#!/usr/bin/env python3

# Dictionsry of characters to Morse Code strings
t2c = {'A':'.-', 
       'B':'-...', 
       'C':'-.-.', 
       'D':'-..', 
       'E':'.', 
       'F':'..-.', 
       'G':'--.', 
       'H':'....', 
       'I':'..', 
       'J':'.---', 
       'K':'-.-', 
       'L':'.-..', 
       'M':'--', 
       'N':'-.', 
       'O':'---', 
       'P':'.--.', 
       'Q':'--.-', 
       'R':'.-.', 
       'S':'...', 
       'T':'-', 
       'U':'..-', 
       'V':'...-', 
       'W':'.--', 
       'X':'-..-', 
       'Y':'-.--', 
       'Z':'--..', 
       '0':'-----', 
       '1':'.----', 
       '2':'..---', 
       '3':'...--', 
       '4':'....-', 
       '5':'.....', 
       '6':'-....', 
       '7':'--...', 
       '8':'---..', 
       '9':'----.',
       '.':'.-.-.-',
       ',':'--..--',
       '?':'..--..',
       '/':'-..-.',
       '@':'.--.-.'}

# Create the code to text dictionary
# Build this in Morse learning order so the printed list 
# is dots to dashes.
c2t = {}
morseLearnText = 'EAWJ1PRLIU2FSV3H45TMO098GQZ7NKYCDXB6.,?/@'
for letter in morseLearnText:
    code = t2c[letter]
    # Create code to text dictionary
    c2t[code] = letter

def printCodeList():
    print('Text to Morse Code table:')
    for letter in t2c:
        code = t2c[letter]
        print(letter + '\t' + code)
    print('\nMorse Code to Text table')
    for code in c2t:
        print(code + '\t' + c2t[code])
    print('')


def usage():
    # Let people know the mode and how to switch it
    print('Hello (.... . .-.. .-.. ---)\n')
    print('There are two modes; Text to Code and Code to Text. The mode is indicated by the prompt.')
    print('The \'TEXT:\' prompt indicates that text will be converted to Morse Code.')
    print('The \'CODE:\' pronpt indicates that code will be converted to text.')
    print('')
    print('The mode is set by entering \'<\' or \'>\'.')
    print(' \'<\' sets the mode to "Code to Text"')
    print(' \'>\' sets the mode to "Text to Code"')
    print(' \'+\' sets \'one line per character output\'. The prompt will change to include a \'+\'.')
    print(' \'-\' sets \'sentence\' mode (the default).')
    print('')
    print('Code is generated and is entered as a sequence of dots (\'.\') and dashes (\'-\').')
    print('One space is between each Morse character and two spaces are between each word.')
    print('')
    print('Entering \'?\' on a line by itself will display this help message.')
    print('Entering \'!\' on a line by itself will display the text to code and code to text list.')

def printt(text):
    print(text, end='')

def getPrompt(textInput, linePerCharMode):
    prompt = ''
    if textInput:
        prompt = 'TEXT'
    else:
        prompt = 'CODE'
    if linePerCharMode:
        prompt = prompt + '+'
    prompt = prompt + ': '
    return prompt

def textToCode(text, linePerCharMode):
    for c in text:
        mc = ' '
        if c in t2c:
            mc = t2c[c]
        elif not c == ' ':
            mc = '*'
        if linePerCharMode:
            print(c + '\t' + mc)
        else:
            printt(mc + ' ')
    print('\n')

def codeToText(code, linePerCharMode):
    codeWords = userInput.split('  ')
    for word in codeWords:
        mc = word.split(' ')
        for c in mc:
            letter = "*"
            if c in c2t:
                letter = c2t[c]
            elif c == '':
                letter = ' '
            if linePerCharMode:
                print(c + '\t' + letter)
            else:
                printt(letter)
    print('\n')

# Print the text-code and code-text lists and the usage.
printCodeList()
usage()
textInput = True
linePerCharMode = False
prompt = getPrompt(textInput, linePerCharMode)

try:
    while True:
        userInput = input(prompt).strip().upper()
        if not userInput:
            # Just prompt again if the input was blank
            continue
        elif userInput == '<':
            textInput = False
            prompt = getPrompt(textInput, linePerCharMode)
            continue
        elif userInput == '>':
            textInput = True
            prompt = getPrompt(textInput, linePerCharMode)
            continue
        elif userInput == '+' and not linePerCharMode:
            linePerCharMode = True
            prompt = getPrompt(textInput, linePerCharMode)
            continue
        elif userInput == '-' and linePerCharMode:
            linePerCharMode = False
            prompt = getPrompt(textInput, linePerCharMode)
            continue
        elif userInput == '?':
            usage()
            continue
        elif userInput == '!':
            printCodeList()
            continue

        # The line entered wasn't one of our commands - convert it...
        if textInput:
            textToCode(userInput, linePerCharMode)
        else:
            codeToText(userInput, linePerCharMode)
except KeyboardInterrupt:
    print('\nGood bye (--. --- --- -..   -... -.-- .)\n')
