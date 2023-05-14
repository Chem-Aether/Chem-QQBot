import requests
import json

def translate(word):
    # 爬取单词翻译
    try:
        url = "https://fanyi.baidu.com/sug"
        da = {
            "kw": word
        }
        re = requests.post(url, data=da)
        data = re.json()['data']
        tips = ''
        for each in data:
            k = each['k']
            v = each['v']
            tips += f'{k}:{v}\n'
        print(tips)
        return tips
    # 如果没有翻译，则输出none
    except:
        return '无翻译内容'

if __name__ == '__main__':
    #translate('背书')
    fy()
