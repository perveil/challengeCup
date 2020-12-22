from bs4 import BeautifulSoup
import pandas as pd
import re
import requests


url = "https://xueqiu.com/hq"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')
div_block = soup.find_all(attrs={'class': 'second-nav'})
li_block = div_block[1].contents[2].find_all('li')
industry2url = {}
health={}
for li in li_block:
    a = li.find('a')
    industry2url[a.get('title')] = url + a.get('href')
    print(li)
    if '医' in a.get('title'):
        print('______________')
        health[a.get('title')]=url+a.get('href')
#用来存储股票对应的公司
dic1={}
infoList = []
for industryKey in health.keys():
    url = health[industryKey][-4:]
    urls=[ 'https://xueqiu.com/service/v5/stock/screener/quote/list?page={}&size=30&order=desc&order_by=percent&exchange=CN&market=CN&ind_code=S'.format(str(i)) + url for i in range(10)]
    for url in urls:
        response = requests.get(url, headers=headers)
        jsonContent = response.json()
        for data in jsonContent['data']['list']:
            dicc={}
            dic={}
            for key in data.keys():
                if key in ['symbol','name']:
                    dic[key] = data[key]
            dicc[dic['symbol']]=dic['name']
            dic1.update(dicc)
            infoList.append(dic)
pd_baseinfo = pd.DataFrame.from_dict(infoList)
pd_baseinfo.to_excel('stock_info/all_about.xlsx')
print(infoList)
print('-----------------')
infoList1=[]
diction={}
for i in dic1.keys():
    if 'SH' in i:
        dicc={}
        dicc[i]=dic1[i]
        diction.update(dicc)
        infoList1.append(dicc)
df1=pd.DataFrame(diction.values(),index=diction.keys())
df1.to_excel(r'stock_info/about_SH.xlsx',index=diction.keys())
