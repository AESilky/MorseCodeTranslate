A simple Python program to encode and decode Morse code.

The program starts in 'Text to Code' mode, with a prompt of 'Text:'.
A line of text will be translated to Morse code. The code will consist 
of '.' (dot) and '-' (dash) with an space between characters and 2 
spaces between words.

For example, the text "HI THERE" will result in a line:
Text: HI THERE
.... ..  - .... . .-. .

The mode can be switched by entering '<' or '>'.
'<' sets the mode to "Code to Text"
'>' sets the mode to "Text to Code"

The prompts are:
'Text:' Text to Code
'Code:' Code to text

Additionally, the output can be set to a single line or to a line 
per character. The line per character prints both the text and 
the code. This is selected by entering a '+' or '-'.
'+' sets the mode to 'line per character' and adds a '+' to the prompt.
'-' sets the mode to single line (the default).

If an unknown charecter is entered in either mode 
the output will be a '*' charachter (not part of the Morse Code).

Entering a single '?' will print usage help. Entering a single '!' 
will print a Text-Code/Code-Text list.

See MORSE.txt for a tab deliminated MORSE-TEXT table.
