#!/usr/bin/env python3

print('MorseConvert - Copyright 2020 Allen Silky\n')
# Licensed under GNU AGPL. See 'COPYING' file for license.


# Dictionsry of text characters to Morse Code strings
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
       '@':'.--.-.',
       ' ':' ', # for conversion, not part of Morse Code
       '*':'*'  # for conversion, not part of Morse Code
       }

# Create the code to text dictionary
# Build this in Morse learning order so the printed list helps people learn. 
c2t = {}
morseLearnText = 'EAWJ1PRLIU2FSV3H45TMO098GQZ7NKYCDXB6.,?/@ *'
for letter in morseLearnText:
    code = t2c[letter]
    # Create code to text dictionary
    c2t[code] = letter


def printCodeList():
    print('Text to Morse Code:')
    for letter in t2c:
        if not letter == ' ' and not letter == '*':
            code = t2c[letter]
            print(letter + '\t' + code)
    print('\nMorse Code to Text')
    for code in c2t:
        if not code == ' ' and not code == '*':
            letter = c2t[code]
            print(code + '\t' + letter)
    print('')


def usage():
    # Let people know the mode and how to switch it
    print('Hello (.... . .-.. .-.. ---)\n')
    print('There are two modes; Text to Code and Code to Text. The mode is indicated by the prompt.')
    print('The \'Text:\' prompt indicates that text will be converted to Morse Code.')
    print('The \'Code:\' pronpt indicates that code will be converted to text.')
    print()
    print('The mode is set by entering \'<\' or \'>\'.')
    print(' \'<\' sets the mode to "Code to Text"')
    print(' \'>\' sets the mode to "Text to Code"')
    print(' \'+\' sets \'one line per character output\'. The prompt will change to include a \'+\'.')
    print(' \'-\' sets \'sentence\' mode (the default).')
    print()
    print('Code is generated and is entered as a sequence of dots (\'.\') and dashes (\'-\').')
    print('One space is between each Morse character and two spaces are between each word.')
    print()
    print('Entering \'?\' on a line by itself will display this help message.')
    print('Entering \'!\' on a line by itself will display the text to code and code to text list.')
    print()
    print('^C to exit.')
    print()


def printt(text):
    print(text, end='')


def getPrompt(textInput, linePerCharMode):
    prompt = ''
    if textInput:
        prompt = 'Text'
    else:
        prompt = 'Code'
    if linePerCharMode:
        prompt = prompt + '+'
    prompt = prompt + ': '
    return prompt


def textToCode(text, linePerCharMode):
    code = ''
    for c in text:
        mc = ' '
        if not c == ' ':
            if c in t2c:
                mc = t2c[c]
            else:
                mc = '*'
        code = code + mc + ' '
    print(code)
    if linePerCharMode:
        for c in text:
            code = "*"
            if c in t2c:
                code = t2c[c]
            print(c + '\t' + code)
    print('\n')


def codeToText(code, linePerCharMode):
    text = ''
    codeWords = userInput.split('  ')
    for word in codeWords:
        mc = word.split(' ')
        for c in mc:
            letter = "*"
            if c in c2t:
                letter = c2t[c]
            elif c == '':
                letter = ' '
            text = text + letter
    print(text)
    if linePerCharMode:
        for c in text:
            print(c + '\t' + t2c[c])
    print('\n')

# Start by printing the text-code and code-text lists and the usage.
printCodeList()
usage()
textInput = True
linePerCharMode = False
prompt = getPrompt(textInput, linePerCharMode)

# Loop reading input lines from the user.
# Process commands and if not a command, convert text-code/code-text.
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
