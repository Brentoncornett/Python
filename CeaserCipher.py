'''
Program: CaesarCipher.py
Author: Brenton Cornett
Purpose: Encrypt or Decrypt by shifting the string indexes based on a key length.

'''

import string # Import string library to generate our character list

# This is the message input by the user to be encrypted or decrypted

message = input("Enter the message to be encrypted or decrypted here: ")
# Ask for key size. if not an int type force user to try again.
while True:
    try:
        key = int(input("Enter the symmetric key size. "))
        break
    except ValueError as error:
        print(errror)
        print("Key must be an int type, please try again.")

#asks the user for the desired mode
mode = input("Enter the mode - [encrypt or decrypt]: ")

#Sets a custom charset of A-Z a-z 0-9 special chars and " "
SYMBOLS = string.ascii_letters + string.digits + string.punctuation + " "

# used to store the output of the program
translated = ""

for symbol in message:   # Loop into every character in message
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol) # Checks index of symbol in our charset
        if mode in ['encrypt', 'Encrypt', 'e', 'E']:
            translatedIndex = symbolIndex + key # if mode is encrypt it adds index by key
        elif mode in ['decrypt', 'Decrypt', 'd', 'D']:
            translateIndex = symbolIndex - key  # if mode is decrypt it subtracts index by key
        translated += SYMBOLS[translatedIndex]
        #Handle wrap around if needed
        if translatedIndex >= len(SYMBOLS):
            translatedIndex -- len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex += len(SYMBOLS)
    #if symbol does not exist in charset, add it to translated
    else:
        translated += symbol

print(translated)
