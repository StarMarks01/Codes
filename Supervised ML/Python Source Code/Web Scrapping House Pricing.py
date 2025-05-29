import requests
import pandas as pd
from bs4 import BeautifulSoup
import re

# print('------------------------------------------------VARIABLES------------------------------------------------')

name = []
price = []
address = []
BHK = [] 
area = []
sq = []
sqft = []
# print('------------------------------------------------URLs------------------------------------------------')

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

# print('------------------------------------------------URLs------------------------------------------------')

url1 = 'https://housing.com/in/buy/searches/M3mP5fuwgucc7a2ear61S0'                         #Vesu data
r1 = requests.get(url1)
soup1 = BeautifulSoup(r1.text,'lxml')

url2 = 'https://housing.com/in/buy/searches/M3mP4eli7i7nb14z32bhS0'                         #Palanpur data
r2 = requests.get(url2)
soup2 = BeautifulSoup(r2.text,'lxml')

url3 = 'https://housing.com/in/buy/searches/M3mP8fhjn37x82c68xcS0'                          #Adajan Data
r3 = requests.get(url3)
soup3 = BeautifulSoup(r3.text,'lxml')

url4 = 'https://housing.com/in/buy/searches/M3mP23g3toylb9ycpcfoS0'                         #Dindoli Data
r4 = requests.get(url4)
soup4 = BeautifulSoup(r4.text,'lxml')

url5 = 'https://housing.com/in/buy/searches/M3mP1ify0w5ka2qjbtopS0'                         #Udhna Zone Data
r5 = requests.get(url5)
soup5 = BeautifulSoup(r5.text,'lxml')

n1 = soup1.find_all('h2',{'class':'T_4d93cd45 _7s5wglyw _1u71grho _gi182v'})
n2 = soup1.find_all('div',{'class':'T_091c165f _sq1l2s _vv1q9c _ks15vq T_3d3547ab _7s5wglyw _5vy24jg8 _blas1v10 new-title'})
p1 = soup1.find_all('div',{'class':'_csbfng _c8f6fq _g3gktf _ldyh40 _7l1ulh T_a6707275'})
n3 = soup2.find_all('h2',{'class':'T_4d93cd45 _7s5wglyw _1u71grho _gi182v'})
n4 = soup2.find_all('div',{'class':'T_091c165f _sq1l2s _vv1q9c _ks15vq T_3d3547ab _7s5wglyw _5vy24jg8 _blas1v10 new-title'})
p2 = soup2.find_all('div',{'class':'_csbfng _c8f6fq _g3gktf _ldyh40 _7l1ulh T_a6707275'})
n5 = soup3.find_all('h2',{'class':'T_4d93cd45 _7s5wglyw _1u71grho _gi182v'})
n6 = soup3.find_all('div',{'class':'T_091c165f _sq1l2s _vv1q9c _ks15vq T_3d3547ab _7s5wglyw _5vy24jg8 _blas1v10 new-title'})
p3 = soup3.find_all('div',{'class':'_csbfng _c8f6fq _g3gktf _ldyh40 _7l1ulh T_a6707275'})
n7 = soup4.find_all('h2',{'class':'T_4d93cd45 _7s5wglyw _1u71grho _gi182v'})
n8 = soup4.find_all('div',{'class':'T_091c165f _sq1l2s _vv1q9c _ks15vq T_3d3547ab _7s5wglyw _5vy24jg8 _blas1v10 new-title'})
p4 = soup4.find_all('div',{'class':'_csbfng _c8f6fq _g3gktf _ldyh40 _7l1ulh T_a6707275'})
n9 = soup5.find_all('h2',{'class':'T_4d93cd45 _7s5wglyw _1u71grho _gi182v'})
n10 = soup5.find_all('div',{'class':'T_091c165f _sq1l2s _vv1q9c _ks15vq T_3d3547ab _7s5wglyw _5vy24jg8 _blas1v10 new-title'})
p5 = soup5.find_all('div',{'class':'_csbfng _c8f6fq _g3gktf _ldyh40 _7l1ulh T_a6707275'})

# print('------------------------------------------------NAME------------------------------------------------')

for i in n1:
    name.append(i.text)
for i in n2:
    name.append(i.text)
for i in n3:
    name.append(i.text)
for i in n4:
    name.append(i.text)
for i in n5:
    name.append(i.text)
for i in n6:
    name.append(i.text)
for i in n7:
    name.append(i.text)
for i in n8:
    name.append(i.text)
for i in n9:
    name.append(i.text)
for i in n10:
    name.append(i.text)

# print('------------------------------------------------PRICE------------------------------------------------')

for i in p1:
    price.append(i.text)
for i in p2:
    price.append(i.text)
for i in p3:
    price.append(i.text)
for i in p4:
    price.append(i.text)
for i in p5:
    price.append(i.text)


# print('------------------------------------------------Addresses------------------------------------------------')

ad1 = soup1.find_all('div',{'class':'T_091c165f _sq1l2s _vv1q9c _ks15vq T_3d3547ab _7s5wglyw _5vy24jg8 _blas1v10 new-title'})
ad2 = soup2.find_all('div',{'class':'T_091c165f _sq1l2s _vv1q9c _ks15vq T_3d3547ab _7s5wglyw _5vy24jg8 _blas1v10 new-title'})
ad3 = soup3.find_all('div',{'class':'T_091c165f _sq1l2s _vv1q9c _ks15vq T_3d3547ab _7s5wglyw _5vy24jg8 _blas1v10 new-title'})
ad4 = soup4.find_all('div',{'class':'T_091c165f _sq1l2s _vv1q9c _ks15vq T_3d3547ab _7s5wglyw _5vy24jg8 _blas1v10 new-title'})
ad5 = soup5.find_all('div',{'class':'T_091c165f _sq1l2s _vv1q9c _ks15vq T_3d3547ab _7s5wglyw _5vy24jg8 _blas1v10 new-title'})

for i in ad1:
    address.append(i.text)
for i in ad2:
    address.append(i.text)
for i in ad3:
    address.append(i.text)
for i in ad4:
    address.append(i.text)
for i in ad5:
    address.append(i.text)

# print('------------------------------------------------BHK NO------------------------------------------------')

pattern = r'(\d+\s*BHK)'

for i in address:
    match = re.search(pattern,i)
    if match:
        BHK.append(match.group(0))

# print(BHK)

# print('------------------------------------------------Areas------------------------------------------------')

for i in address:
    a = i.split()[-1]
    area.append(a)
# print(area)

# print('------------------------------------------------DataFrame------------------------------------------------')

sq1 = soup1.find_all('div',{'class':'T_1e5d5ecb _e214no T_ad2d45b4 _9s1txw T_9473b29c _5j1tlg _0h1h6o _vy18a8 _be1g80 _2621jn item-container'})
sq2 = soup2.find_all('div',{'class':'T_1e5d5ecb _e214no T_ad2d45b4 _9s1txw T_9473b29c _5j1tlg _0h1h6o _vy18a8 _be1g80 _2621jn item-container'})
sq3 = soup3.find_all('div',{'class':'T_1e5d5ecb _e214no T_ad2d45b4 _9s1txw T_9473b29c _5j1tlg _0h1h6o _vy18a8 _be1g80 _2621jn item-container'})
sq4 = soup4.find_all('div',{'class':'T_1e5d5ecb _e214no T_ad2d45b4 _9s1txw T_9473b29c _5j1tlg _0h1h6o _vy18a8 _be1g80 _2621jn item-container'})
sq5 = soup5.find_all('div',{'class':'T_1e5d5ecb _e214no T_ad2d45b4 _9s1txw T_9473b29c _5j1tlg _0h1h6o _vy18a8 _be1g80 _2621jn item-container'})
for i in sq:
    sq.append(i.text)
for i in sq2:
    sq.append(i.text)
for i in sq3:
    sq.append(i.text)
for i in sq4:
    sq.append(i.text)
for i in sq5:
    sq.append(i.text)
# print(sq)

sqft_pattern = r'Builtup area(\d+(\.\d+)?)\s*sq\.ft'

for i in sq:
    match = re.search(sqft_pattern,i)
    if match:
        sqft.append(match.group())
    else:
        sqft.append(None)
# print(sqft)

# print(len(name))
# print(len(address))
# print(len(price))
# print(len(BHK))
# print(len(sq))

df = pd.DataFrame(list(zip(BHK,price,area,sqft)),columns=['BHK NO','Price','Area','Square feet'])
print(df)