import requests
import json

api_key = 'SWSn4brixEZOHSR-4'
def Change_Date(date,STR):
    L = date.split(STR)
    try:
        year = L[0]
        month = int(L[1])
        day = int(L[2])
        return f'{year}年{month}月{day}日'
    except:
        return None


def get_HourWeather(location='西安',hours=2):
    url = f'https://api.seniverse.com/v3/weather/hourly.json?key={api_key}&location={location}&language=zh-Hans&unit=c&start=0&hours={hours}'
    res = requests.get(url)

    tips = f'{location}未来{hours}小时天气预测如下：\n'
    for time,each in enumerate(json.loads(res.text)['results'][0]['hourly'],1):
        text = each['text']
        temperature = each["temperature"]
        humidity = each["humidity"]
        wind = each["wind_direction"]
        wind_speed = each["wind_speed"]
        tips += f'{time}时天气{text}，温度{temperature}℃，相对湿度{humidity}%，风向{wind}，风速{wind_speed}km/h\n'
    print(tips)
    return  tips

def get_DayWeather(location='西安',days=3):
    url = f'https://api.seniverse.com/v3/weather/daily.json?key={api_key}&location={location}&language=zh-Hans&unit=c&start=0&days={days}'
    res = requests.get(url)
    #print(res.text)
    tips = f'{location}未来{days}天天气预测如下：\n'
    for each in json.loads(res.text)['results'][0]['daily']:
        date = each['date']
        text_day = each['text_day']
        text_night = each['text_night']
        high = each['high']
        low = each['low']
        precip = each['precip']
        humidity = each['humidity']
        tips += f'{date}:白天{text_day}，夜间{text_night}，气温{high}℃-{low}℃，降水概率{precip}%，相对湿度{humidity}%\n'
    print(tips)
    return tips

def get_Today_Culture(start=0):
    url = f'https://api.seniverse.com/v3/life/chinese_calendar.json?key={api_key}&start={start}&days=1'
    req = json.loads(requests.get(url).text)['results']['chinese_calendar'][0]

    date = Change_Date(req['date'],'-')
    zodiac = req['zodiac']
    ganzhi_year = req['ganzhi_year']
    lunar_year = req['lunar_year']
    lunar_month = req['lunar_month']
    lunar_day = req['lunar_day']
    lunar_month_name = req['lunar_month_name']
    lunar_day_name = req['lunar_day_name']
    if start == 0:
        tips = f'今天是{date}，农历{ganzhi_year}{zodiac}年{lunar_month_name}{lunar_day_name}'
    elif start == -1:
        tips = f'昨天是{date}，农历{ganzhi_year}{zodiac}年{lunar_month_name}{lunar_day_name}'
    elif start ==1:
        tips = f'明天是{date}，农历{ganzhi_year}{zodiac}年{lunar_month_name}{lunar_day_name}'
    else:
        tips = f'{date}是农历{ganzhi_year}{zodiac}年{lunar_month_name}{lunar_day_name}'
    print(tips)
    return tips

def ad():
    url = f'https://api.seniverse.com/v4?fields=weather_hourly_1h_global&key={api_key}&locations=beijing'
    req = json.loads(requests.get(url).text)
    print(req)


L = ['西安','3']
B = ['2022/1/2']
if __name__ == "__main__":
    #get_HourWeather(location='西安',hours=3)
    #get_HourWeather(*L)
    #get_DayWeather(*L)
    print(Change_Date('2000/02/02','/'))

    get_Today_Culture(*B)

    ad()
