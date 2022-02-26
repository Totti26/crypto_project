#cryptoproject

alphabet = 'abcdefghijklmnopqrstuvwxyz'


def encrypt(message, num):
    endMessage = ''
    for letter in message:
        newIndex = letterToNum(letter) + int(num)
        if newIndex > 25:
            newIndex -= 26
        endMessage += alphabet[newIndex]
    return endMessage


def decrypt(message, num):
    endMessage = ''
    for letter in message:
        newIndex = letterToNum(letter) - int(num)
        if newIndex < 0:
            newIndex += 26
        endMessage += alphabet[newIndex]
    return endMessage


def letterToNum(letter):
    i = 0
    for let in list(alphabet):
        if letter == let:
            return i
        i += 1 



action = input('Would you like to encrypt or decrypt a message? ')
inputing = True
while inputing:
    message = input('Enter the message: ')
    for letter in message:
        if letter not in alphabet:
            inputing = True
            break
        else:
            inputing = False

while True:
    num = input('What is the number: ')
    if len(num) != 1:
        continue
    elif num in '123456789':
        break

if action == 'encrypt':
    print(encrypt(message, num))
if action == 'decrypt':
    print(decrypt(message, num))
