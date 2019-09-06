# -*- coding: utf-8 -*-
# Author By:ice
import json
import requests
import time
import datetime
from fake_useragent import UserAgent
from prettytable import PrettyTable
def vulinfo():
    ua = UserAgent(verify_ssl=False)
    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    yesterday = datetime.date.today() + datetime.timedelta(-1)
    today = time.strftime("%m%d", time.localtime())
    x = PrettyTable(["厂商名称", "漏洞类型", "危险等级", "公布时间"])
    for i in range(0,20):
        r = requests.get('https://www.butian.net/Loo/index/p/'+str(i)+'.html',headers=headers).text
        r = json.loads(r)

        for i in r['data']['list']:
                 title = i['title']
                 level = i['level']
                 dtime = i['datetime']
                 attribute = i['attribute']
                 title = str(title+' '+level+' '+dtime+attribute).replace('发现了','').replace('的一个',' ')
                 title = title.split(' ')
                 print(title[0]+title[1]+title[2]+title[3])
                 if title[3]==str(yesterday):
                     return 1
                 else:
                     x.add_row([title[0], title[1], title[2], title[3]])
                     with open(today+'-vulinfo'+'.txt','w') as f:
                      f.write(str(x)+'\n')
if __name__ == '__main__':
    vulinfo()
    print('It has finished!')