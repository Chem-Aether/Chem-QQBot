import requests
from bs4 import BeautifulSoup

def get_News():
    # 请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53',
        'Host': 'jwc.nwu.edu.cn',
    }
    # 发送url请求
    url = 'https://jwc.nwu.edu.cn/'
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')

    # 最新消息
    news = soup.body.find_all(class_="main2-list fl")[0]
    sort = news.find_all(class_="main2-l")[0].string
    massage = news.find_all(target="_blank")[1].string
    when = news.find_all(class_="main2-d")[0].string
    web = url + news.find_all(name='a')[1].attrs['href']
    tips = '学校教务处最新通知：\n时间：' + when + '\n类别：' + sort + '类\n通知概要：' + massage + '\n原文链接：' + web + "\n" + '-' * 50
    print(tips)
    return str(tips)

if __name__ == "__main__":
    pass