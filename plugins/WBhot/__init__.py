import json

import requests


def get_WbHot(N=10):
    url = 'https://weibo.com/ajax/side/hotSearch'
    req = json.loads(requests.get(url).text)['data']
    #print(req)
    tips = ''
    current_politicsreq = req['hotgovs'][0]
    name = current_politicsreq['name'].strip("#")
    url = current_politicsreq['url']
    tips += f'时政要闻：{name}\n链接：{url}'
    for each in req['realtime'][0:int(N)]:
        try:
            category = each['category']
            note = each['note']
            hot = each['raw_hot']
            label = each['label_name']
            rank = each['rank']+1
            tips += f'\n{rank}:{note}-{label}({hot})-{category}类'
        except:
            pass
    print(tips)

    return tips
if __name__ == "__main__":

    get_WbHot(3)