import random
import string


def generateKey():
    key = random.choices(string.ascii_lowercase, k=3)
    return key


print(generateKey())
