import json
import os
import random
import string
import requests
import datetime
from allure_commons._allure import attach
from allure_commons.types import AttachmentType

'''Для поиска кода для телефона'''
phone_request = None
code = None
def get_sms_data():
    global phone_request, code
    response = requests.get('https://debug.gepur.org/rapi/sms/log')
    if response.status_code == 200:
         data = json.loads(response.text)
         phone_request = data[0]['recipient']
         code = data[0]['text_short']
         return phone_request, code
    else:
        print('Ошибка:', response.status_code)
        return None, None
def get_code():
    return (code)

'''Рандомный юзернейм'''
lst = random.randint(1000000, 9999999)
user = "User"
user_random = user + str(lst)

'''Рандомный телефон'''
phone = "+38073"
number = random.randint(1000000, 9999999)
phone_number = phone + str(number)


phone2 = "+38067"
number2 = random.randint(1000000, 9999999)
phone_number2 = phone2 + str(number)


'''Рандомный email'''
random_email = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
random_email2 = ''.join(random.choices(string.ascii_letters + string.digits, k=20))

