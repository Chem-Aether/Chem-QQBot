import requests
import hashlib
import time

def youdao():
    localtime = str(int(time.time() * 1000))
    data = f"client=fanyideskweb&mysticTime={localtime}&product=webfanyi&key=fsdsogkndfokasodnaso"
    sign = hashlib.md5(data.encode(encoding='utf-8')).hexdigest()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
        "Referer": "https://fanyi.youdao.com/index.html"
    }
    cookies = {
        "OUTFOX_SEARCH_USER_ID": "-2094880112@10.108.162.135",
        "OUTFOX_SEARCH_USER_ID_NCOO": "86107500.53660281"
    }
    url = "https://dict.youdao.com/webtranslate"
    word = input('请输入翻译内容:')
    data = {
        "i": f"{word}",
        "from": "auto",
        "to": "",
        "dictResult": "true",
        "keyid": "webfanyi",
        "sign": sign,
        "client": "fanyideskweb",
        "product": "webfanyi",
        "appVersion": "1.0.0",
        "vendor": "web",
        "pointParam": "client,mysticTime,product",
        "mysticTime": localtime,
        "keyfrom": "fanyi.web"
    }
    response = requests.post(url=url, headers=headers, cookies=cookies, data=data).text
    print(response)



def baidu():
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42'
    }
    data = {
        'from': 'en',
        'to': 'zh',
        'query': 'revert',
        'transtype': 'translang',
        'simple_means_flag': '3',
        'sign': '82229.369156',
        'token': 'e0f19b89021dc29b223aafdfd2e93263',
        'domain': 'common',
        'ts': str(int(time.time() * 1000)),
    }
    url = "https://fanyi.baidu.com/v2transapi"
    req = requests.post(url=url,headers=header,data=data)
    print(req.text)
    print(str(int(time.time() * 1000)))

if __name__ == '__main__':
    baidu()