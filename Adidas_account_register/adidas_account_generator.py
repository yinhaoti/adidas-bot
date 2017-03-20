import json
import os
import random
import requests
import string
from bs4 import BeautifulSoup
from requests_toolbelt import MultipartEncoder

from Adidas_account_register.GmailDotEmailGenerator import GmailDotEmailGenerator

with open('accountApp_config.json') as json_data_file:
    data = json.load(json_data_file)

FirstName = data['INFO']['First_Name']
LastName = data['INFO']['Last_Name']
Month = data['INFO']['Month']
Day = data['INFO']['Day']
Year = data['INFO']['Year']
Password = data['INFO']['Passwords']
Gender = data['INFO']['Gender']
Email_prefix = data['SYS']['Email_prefix']
NumberOfAccount = data['SYS']['NumberOfAccount']

def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, sdch, br',
        'Accept-Language': 'en-GB,en-US;q=0.8,en;q=0.6',
        'Upgrade-Insecure-Requests': '1'
    }

    s = requests.Session()
    # print('row header', s.headers)
    s.headers.update(headers)
    r = s.get('https://www.adidas.com.cn/customer/account/create/')
    # print(BeautifulSoup(r.text, "html.parser"))
    csrftoken = BeautifulSoup(r.text, "html.parser").find('input', {'name': 'token'}).get('value')

    email_list = GmailDotEmailGenerator(Email_prefix + '@gmail.com').generate()[:NumberOfAccount]


    for email in email_list:

        username = random_username_generator()
        phoneNum = random_num_generator(11)

        m = MultipartEncoder(fields={
            'token': csrftoken,
            'firstname': FirstName,
            'mobile': phoneNum,
            'gender': Gender,
            'day': Day,
            'year': Year,
            'dob': Year+'-'+Month+'-'+Day,
            'osolCatchaTxt': random_num_generator(5),
            'osolCatchaTxtInst': '1',
            'email': email,
            'username': username,
            'password': Password,
            'confirmation': Password,
            'agree_terms': '1'
        })

        s.headers.update({
            'Origin': 'https://www.adidas.com.cn',
            'Referer': 'https://www.adidas.com.cn/customer/account/create/',
            'Content-Type': m.content_type
        })

        r = s.post('https://www.adidas.com.cn/customer/account/createpost/', data=m)

        print(r.status_code)

        soup = BeautifulSoup(r.text, "html.parser")

        valid_regi = soup.find('p',{'class': 'alertBoxCont'})
        if valid_regi == None:
            print('register success')
            print("Created Account : Username = {0}, Password = {1}".format(email, 'asdfasdf'))
            with open('accounts' + '.txt', 'a') as f:
                f.write(email + ':' + 'asdfasdf' + '\n')
                f.close()
        else:
            print(valid_regi)
            with open('./adidas.html', 'wb') as f:
                f.write(r.content)





def random_num_generator(length):
    numbers = string.digits
    random.seed = (os.urandom(1024))
    phoneNum = ''.join(random.choice(numbers) for i in range(length))
    return phoneNum

def random_username_generator():
    length = 13
    chars = string.ascii_lowercase + string.digits + '_'
    random.seed = (os.urandom(1024))
    name = ''.join(random.choice(chars) for i in range(length))
    return name

if __name__ == '__main__':
    main()
