import requests
import json

import matplotlib.pyplot as plt


api_key = 'SWSn4brixEZOHSR-4'

def get_DayWeather(location='西安',days=3):
    url = f'https://api.seniverse.com/v3/weather/daily.json?key={api_key}&location={location}&language=zh-Hans&unit=c&start=0&days={days}'
    res = requests.get(url)
    #print(res.text)
    tips = f'{location}未来{days}天天气预测如下：\n'
    years = []
    turnovers = []
    for each in json.loads(res.text)['results'][0]['daily']:
        date = each['date']
        text_day = each['text_day']
        text_night = each['text_night']
        high = each['high']
        low = each['low']
        precip = each['precip']
        humidity = each['humidity']
        years.append(date)
        turnovers.append(int(high))
        tips += f'{date}:白天{text_day}，夜间{text_night}，气温{high}℃-{low}℃，降水概率{precip}%，相对湿度{humidity}%\n'
    print(tips)
    plt.figure(figsize=(10, 10), dpi=100)
    plt.scatter(years, turnovers)
    plt.show()
    return tips








L = ['西安','16']
B = ['2022/1/2']
if __name__ == "__main__":
    get_DayWeather(*L)
