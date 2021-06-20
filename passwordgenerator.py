## Python Password Generator

import random
import string

def generatepassword():

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation

    all = lower + lower.upper() + numbers + symbols
    length = 16
    password = ''.join(random.sample(all, length))

    return password

print (generatepassword())

## OUTPUT => x1gQ-.Ju{]F3c8YI


