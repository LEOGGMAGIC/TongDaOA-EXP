import requests
import re
import time

RED = '\x1b[1;91m'
CYAN = '\033[1;36m'
GREEN = '\033[1;32m'
BOLD = '\033[1m'
END = '\033[0m'

def get_version(host): # 获取通达版本信息(全版本)
    content = ''
    print(CYAN + '[->] 正在获取目标的版本信息' + END)
    url = host + 'inc/expired.php'
    response = requests.get(url=url,timeout=2)
    if response.status_code == 200 and 'Office' in response.text:  
        pattern = re.compile('<td class="Big"><span class="big3">(.*?)</span>',re.S)
        info = re.findall(pattern,response.text)
        content += '[*] 获取目标版本成功，版本信息如下：' + '\n'
        content += info[0].replace('<br>','').replace(' ','')
        print(GREEN + content + END)
        return content
    else:
        content += '[-] 未发现版本信息' + '\n'
        print(RED + content + END)
        return content

def run(host):
    get_version(host)
