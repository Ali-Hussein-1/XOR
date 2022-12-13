import random
import string


def generateKey():
    key = random.choices(string.ascii_lowercase, k=3)
    return key


print(generateKey())

# function to decrypt the code


def decryptKey(code):
    # spliting the code into a list of integers
    L = code.split(',')
    # converting the list of integers into a list of characters
    for i in range(len(L)):
        L[i] = int(L[i])
        chars = []
        chars[i] = chr(L[i])
