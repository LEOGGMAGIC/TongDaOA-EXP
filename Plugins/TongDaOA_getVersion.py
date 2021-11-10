import requests
import re
import time

def get_version(host): # 获取通达版本信息(全版本)
    content = ''
    content += '[->] 正在获取目标的版本信息' + '\n'
    url = host + 'inc/expired.php'
    try:
        response = requests.get(url=url,timeout=2)
        pattern = re.compile('<td class="Big"><span class="big3">(.*?)</span>',re.S)
        info = re.findall(pattern,response.text)
        content += '[*] 获取目标版本成功，版本信息如下：' + '\n'
        content += info[0].replace('<br>','').replace(' ','')
        print(content)
        return content
    except:
        content += '[-] 未发现版本信息' + '\n'
        print(content)
        return content

def run(host):
    get_version(host)
