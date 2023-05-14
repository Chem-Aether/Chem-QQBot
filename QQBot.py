import plugins.JWC as JWC
import plugins.weather as Weather
import plugins.translate as Translate
import plugins.WBhot as WB
import Help

from flask import Flask, request
from flask_frozen import Freezer
import requests
import re

app = Flask(__name__)

def SendMesg(url,text,Mesg_type):
    print(request.get_json().get('message_type'))
    if Mesg_type == 'private':
        print(request.get_json().get('user_id'), type(request.get_json().get('user_id')))
        datas = {
            'message_type': str(request.get_json().get('message_type')),
            'user_id': '3254806570',
            'message': text
        }
        requests.post(url=url, data=datas)

    if Mesg_type == 'group':
        print(request.get_json().get('group_id'), type(request.get_json().get('group_id')))
        datas = {
            'message_type': request.get_json().get('message_type'),
            'group_id': str(request.get_json().get('group_id')),
            'message': text
        }
        requests.post(url=url, data=datas)

def Listener(text):
    try:
        L = text.split('#')
        if re.search(L[0], text):
            a = map[L[0]](*L[1:])
            SendMesg(url='http://127.0.0.1:5700/send_msg', text=a, Mesg_type=request.get_json().get('message_type'))
        else:
            print('不是命令')
    except:pass

map = {

}
def add(name,fun):
    map[name] = fun


add('/ls',Help.get_Cmd_List)
add('/help',Help.get_Help)


add('/tqh', Weather.get_HourWeather)
add('/tqd',Weather.get_DayWeather)
add('/nl',Weather.get_Today_Culture)
add('/jwc',JWC.get_News)
add('/fy',Translate.translate)
add('/rs',WB.get_WbHot)

@app.route('/', methods=["POST", "GET"])
def index():
    Listener(request.get_json().get('message'))
    return ''

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=8080)
#print(plugins.JWC.get_News())