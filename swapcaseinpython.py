

string1 = 'CODEwithJoxia'
string2 = 'PythonCoder'

def swap_case(s):
    
    result = ''
    
    for char in s:
        if(char.isupper()==True):
            result += (char.lower())
        elif(char.islower()==True):
            result += (char.upper())
        else:
            result += char
    return result


print (swap_case(string1))
print (swap_case(string2))