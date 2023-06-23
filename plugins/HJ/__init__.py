import datetime
import time


def get_DDL_SX():
    now_t = time.localtime()
    ddl = datetime.datetime(2023,7,1,13,30,0)
    noww = datetime.datetime.now()
    timedelta =ddl-noww

    tips = f'现在是{time.strftime("%Y年%m月%d日 %H:%M:%S", now_t) }，距离实习结束还有{timedelta.days}天，累计{int(timedelta.days*24 + timedelta.seconds/3600)}小时，{timedelta.days*24*3600 + timedelta.seconds}秒'
    print(tips)
    return tips

if __name__ == "__main__":
    get_DDL_SX()