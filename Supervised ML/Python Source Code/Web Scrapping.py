import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops'
r = requests.get(url)
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
# print(r.text)
# print(r.status_code)
# print(r)

soup = BeautifulSoup(r.text,'lxml')
lprice = soup.find('h4',{'class':'price float-end card-title pull-right'})

# print(lprice.text)


aprice = soup.find_all('h4',{'class':'price float-end card-title pull-right'})

# print(aprice)
# l=[i.text for i in aprice]
# print(l)

Price = []

for i in aprice:
    Price.append(i.text)

# print(Price)

aratings = soup.find_all('p',{'class':'review-count float-end'})
# print(aratings)

ratings = []
for i in aratings:
    ratings.append(i.text)

adesc = soup.find_all('p',{'class':'description card-text'})
# print(acompany)

description = []
for i in adesc:
    description.append(i.text.split()[0])

desc = []
for i in adesc:
    desc.append(i.text)

# print(desc)
df = pd.DataFrame(list(zip(description,Price,ratings)),columns = ['Name','Price','Ratings'])
print(df)

