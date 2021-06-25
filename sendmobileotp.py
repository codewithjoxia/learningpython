## Python Send OTP to Mobile

import random
import string
import requests

def generateotp():
    numbers = str(random.randrange(100001, 999999))
    str_var = list(string.ascii_uppercase)
    random.shuffle(str_var)
    letters = ''.join(str_var)
    otp = letters[0:3] + "-" + numbers   

    body = "Use this OTP {} to verify your account".format(otp)
    
    print (body)

    return body

def bulksmsnigeria_module(phone_number, sender_name):
    my_api_token =  # Get your API_Key from www.bulksmsnigeria.com 
    
    if sender_name.strip() == '':
        sender_name = 'Joxia'

    url = "https://www.bulksmsnigeria.com/api/v1/sms/create?api_token={_api_token}&from={_sender_name}&to={_phone_number}&body={_message}&dnd=2"
    url = url.format(_api_token = my_api_token, _sender_name = sender_name, _phone_number = phone_number, _message=generateotp())
    
    response = requests.post(url)
    
    return response.json()['data']['status']

#send SMS module
status = bulksmsnigeria_module("2348020", 'Joxia')

print (status)

#follow insta/@codewithjoxia