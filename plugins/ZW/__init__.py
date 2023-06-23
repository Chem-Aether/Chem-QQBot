import requests
from bs4 import BeautifulSoup
import json

def get_link(name):
    url = f'http://db.kib.ac.cn/CNFlora/SearchEngine.aspx?q={name}'
    req = requests.get(url).text.replace('\r\n','')
    soup  = BeautifulSoup(req, features="html.parser").find(class_="table table-bordered")
    #print(soup.contents)
    ALL = []
    for each in soup:
        try:
            #print(each)
            j =[i for i in each.contents if i!=' ']
            if '种' in j[5].string:
                K = j[1].string
                zh_name = j[3].string
                en_name = j[4].string
                rank = j[5].string
                link = j[4].a.attrs['href']
                ALL.append(
                    {'zh_name':zh_name,
                     'en_name':en_name,
                     'K':K,
                     'link':link
                    })
                #print(K,zh_name,en_name,rank,link)
        except:pass
    return ALL

def get_Msg(name):
    text = get_link(name)
    lens = len(text)
    url = ''
    if lens!=0:
        for each in text:
            if str(each['zh_name']) == str(name):
                link = each['link']
                url = f'http://db.kib.ac.cn/CNFlora/{link}'
                zh_name = each['zh_name']
                en_name = each['en_name']
                k = each['K']
                break
        try:
            req = requests.get(url)
            soup = BeautifulSoup(req.text, features="html.parser")
            tips = f'{zh_name}\n{en_name}'
            family = soup.find(class_='breadcrumb nomargin').find_all('li')
            #print(family)
            for each in family[2:-1]:
                tips = tips + '\n' + each.a.string
            a = [j for j in soup.find(id="ContentPlaceHolder1_lbl_fulltext").string.split('  ') if j != ''][2:]
            for each in a:
                t = each.replace('\r\n', '').replace(' ', '')
                tips += f'\n{t}'
            print(tips)

            img = soup.find(id='ContentPlaceHolder1_img_pic')
            print(img)
            CQ=''
            if img!=None:
                picture = img.attrs['src']
                CQ = f'[CQ:image,file={picture},id=40000]'
                print(CQ)
            return tips + CQ
        except:
            tips = '详细科属信息如下：请选择（有重复可使用link查询）：'
            for each in text:
                zh_name = each['zh_name']
                en_name = each['en_name']
                link = text[0]['link']
                tips += f'\n{zh_name}-{en_name}\nlink:{link}'
            print(tips)
            return tips
    else:
        print('查无此植物')
        return '查无此植物'

if __name__ == "__main__":
    #get_link('光核桃')
    get_Msg('白花过路黄')
    #get()
    # http://db.kib.ac.cn/CNFlora/SearchResult.aspx?cpni=CPNI-299-29885