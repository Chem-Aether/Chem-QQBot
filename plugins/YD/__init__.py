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
    try:
        url = 'https://db2.ouryao.com/yd2020/'+ get_Link(name)
        req=requests.get(url=url)
        req = req.text.replace('<sub>','').replace('</sub>','').replace('\u3000\u3000','').replace('\r\n','').replace('<sup>','').replace('</sup>','').replace('</b><b>','')
        soup = BeautifulSoup(req,features="html.parser")

        table = soup.find(class_="cms_list").div

        List_after = []
        for i in table.pre.contents:
            if i.string!=None:
                List_after.append(i.string)

        if ((len(List_after)-3))%2==0:
            i=3
            ALL=['【中文名称】',table.contents[1].string,'【拼音名称】',table.contents[3].string,'【英文名称】',table.contents[5].string]+List_after[3:]
        else:
            i=4
            ALL=['【中文名称】', table.contents[1].string, '【拼音名称】', table.contents[3].string, '【英文名称】', table.contents[5].string]+['【简介】',List_after[3]]+List_after[4:]
        return ALL
    except:
        print('查询失败')
        return None

def creat_String(name):
    try:
        L=get_Meg(name)
        i=0
        tips=''
        while i<len(L):
            tips+=f'{L[i]}{L[i+1]}\n'
            i+=2
        #print(tips)
        return tips
    except:
        print('查询失败')
        return None


if __name__ == "__main__":
    creat_String('黄柏')




