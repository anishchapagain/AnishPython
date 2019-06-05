#import csv
#from urllib.request import urlopen
import requests
#from pyquery import PyQuery as pq
import time

BASE_URL = "http://hamrobazaar.com/"

#def read_url(url,username,password):
requestHeaders={
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'en-US,en;q=0.8',
    'Connection':'keep-alive',
    'Host':'hamrobazaar.com',
    'Referer':'https://hamrobazaar.com/member_login.php',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}
r= requests.get('http://hamrobazaar.com/index.php')
print(r.status_code)
print(r.headers)
#requests.get('https://hamrobazaar.com/member_login.php')

login = {'username':'ayuzawa925@gmail.com',
'password':'furukawa',
'redirect_to':'https://hamrobazaar.com/member.php',
'submit':'Member Login'
}

html= requests.post('https://hamrobazaar.com/member_login.php',data=login)#.content#,headers=requestHeaders)
print(html.text)
time.sleep(5)
html = requests.get('https://hamrobazaar.com/member.php')
#html = requests.get('https://hamrobazaar.com/index.php')#.content
print(html.text)
quit()