import re

import requests
from bs4 import BeautifulSoup


def get_Link(name):
    try:
        url_key = f'https://db2.ouryao.com/yd2020/index.php?k={name}'
        req = requests.get(url=url_key)
        soup = BeautifulSoup(req.text, features="html.parser")
        link = soup.body.find(class_="datarow").a.attrs['href']
        #print(link)
    except:
        link = None
        print('查无此药')
    return link

def get_Meg(name='知母'):
    url = 'https://db2.ouryao.com/yd2020/'+ get_Link(name)
    req=requests.get(url=url)
    req = req.text.replace('<sub>','').replace('</sub>','').replace('\u3000','').replace('\r\n','').replace('<sup>','').replace('</sup>','').replace('</b><b>','')
    soup = BeautifulSoup(req,features="html.parser")

    table = soup.find(class_="cms_list").div

    #前缀文字列表
    a = ['【中文名称】', table.contents[1].string, '【拼音名称】', table.contents[3].string, '【英文名称】',table.contents[5].string]
    a = ['无' if i is None else i for i in a]
    #合并总表
    S = [i.string for i in table.pre.contents if i.string!=None]
    if re.search(r'[【](.*)[】]', S[0]):
        S = a+S
    else:
        a.append('【简介】')
        S = a + S
    #print(S)
    #规整列表
    ALL=[]
    i=0
    try:
        while i<(len(S)-1):
            t = S[i]
            n=''
            for each in S[i+1:]:
                if re.search(r'[【](.*)[】]', each):
                    i+=1
                    break
                else:
                    n+=each
                    i+=1
            ALL.append([t,n])
    except:pass
    #print(ALL)
    return ALL


def creat_String(name):
    try:
        L=get_Meg(name)
        i=0
        tips=''
        for each in L:
            tips +=f'{each[0]}{each[1]}\n'
        print(tips)

        if len(tips)<1800:
            return tips
        else:
            return tips[:1800]
    except:
        return "查无此药"

if __name__ == "__main__":
    creat_String('黄柏')




