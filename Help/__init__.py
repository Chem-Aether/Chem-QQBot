import json


with open('./Help/Help.json',encoding='utf-8') as f:
    Help_json = json.load(f)

def get_Cmd_List():
    tips = '命令列表：'
    for each in Help_json['content']:
        tips += f'\n{each}'
    print(tips)

    return tips

def get_Help(cmd='help'):
    try:
        return Help_json['content'][cmd]
    except:pass

if __name__ == "__main__":
    get_Cmd_List()
    print(get_Help('/tqh'))