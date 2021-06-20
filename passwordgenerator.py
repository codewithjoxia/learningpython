## Python Password Generator

import random

def generatepassword():

    lower = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '1234567890'
    symbols = '[]{}()*;/,.-_'

    all = lower + lower.upper() + numbers + symbols
    length = 16
    password = ''.join(random.sample(all, length))

    return password

print (generatepassword())

## OUTPUT => x1gQ-.Ju{]F3c8YI


