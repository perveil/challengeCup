import pandas as pd
import json
import requests


headers = {
    'Accept': '*/*',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Cookie': 'yfx_c_g_u_id_10000042=_ck20121715350419051539379751535; yfx_f_l_v_t_10000042=f_t_1608190504898__r_t_1608190504898__v_t_1608190504898__r_c_0; VISITED_MENU=%5B%228352%22%5D; VISITED_STOCK_CODE=%5B%22600829%22%5D; VISITED_COMPANY_CODE=%5B%22600829%22%5D; seecookie=%5B600829%5D%3A%u4EBA%u6C11%u540C%u6CF0; JSESSIONID=B2C73F872C7BD95AB1E6DD2E39D9E5DF',
    'Host': 'query.sse.com.cn',
    'Referer': 'http://www.sse.com.cn/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}
stock_ii=[]
stock_information={}
company2filelist={}
aimStocklist= pd.read_excel('./stock_info/about_SH.xlsx',engine='openpyxl').values
#从excel中读取股票的代码
for i in aimStocklist:
    url='http://query.sse.com.cn/security/stock/queryCompanyBulletin.do?jsonCallBack=jsonpCallback80405&isPagination=true&productId='+str(i[0])[2:]+'&securityType=0101&reportType2=DQBG&reportType=ALL&beginDate=2020-09-19&endDate=2020-12-18&pageHelp.pageSize=25&pageHelp.pageCount=50&pageHelp.pageNo=1&pageHelp.beginPage=1&pageHelp.cacheSize=1&pageHelp.endPage=5&_=1608190505623'
    response = requests.get(url, headers=headers)
    content2json=json.loads(response.content[19:len(response.content)-1])
    print(content2json)
    #content2json数据类型是字典
    filelist=[]
    list=[]
    #用来查看所存储数据的类型
    stock_information.update(content2json)
    if len(content2json['pageHelp']['data'])==0:
        company2filelist[str(i[1])] = filelist
        print(str(i[1]))
        #比如说是,在为空的情况下输出，eg: 健之康 开开B股
        continue
    for file in content2json['pageHelp']['data']:
        if '正文' not in file['TITLE']:
            filelist.append(file['URL'])
    if len(filelist)==2:
        filelist=[]
    count=0
    for file in content2json['pageHelp']['data']:
        count=count+1
        if len(filelist)==0:
            if count==2:
                filelist.append(file['URL'])
    company2filelist[str(i[1])]=filelist
df=pd.DataFrame(company2filelist.values(),index=company2filelist.keys())
df.to_excel(r'index/inde_xabout_SH_test.xlsx',index=company2filelist.keys())


for i in company2filelist.keys():
    filelist=company2filelist[i]
    if len(filelist)==0:
        continue
    for file in filelist:
     fileRequest=requests.get('http://www.sse.com.cn/'+file)
     nameLen=len(str(file).split('/'))
     filename=str(file).split('/')[nameLen-1]
     with open('./pdf/'+str(i).replace('*','')+'-'+filename, "wb") as f:
         f.write(fileRequest.content)
print(company2filelist)
