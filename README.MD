# 通达OA系列检测EXP

检测模块集成在Plugins文件夹内

稍微改了一下这位大佬的exp`https://github.com/kitezzzGrim/tongda-exp`

有新的检测模块欢迎交流学习~

# 使用方法

```
python TongDaOA.py
```

python3

根据提示输入URL地址：`http://xxx.xxx.xxx.xxx:xxxx/`，注意URL最后带上`/`

一键检测，测试案例如下（通达V11.2）

![image-20211110105941832](https://image-1303962289.cos.ap-beijing.myqcloud.com/image-20211110105941832.png)

![image-20211110105956317](https://image-1303962289.cos.ap-beijing.myqcloud.com/image-20211110105956317.png)

## 获取版本信息

检测`inc/expired.php`是否存在版本信息泄露

## 空口令登录

使用空口令尝试登陆

## 通达<11.3任意文件包含漏洞

检测是否存在文件包含漏洞

如果存在尝试读取`general/../../mysql5/my.ini`

## 通达<11.3文件上传+文件包含getshell

先检测是否存在文件包含漏洞，如果存在直接上🐎

存在漏洞会在这个目录生成冰蝎默认马`ispirit/interface/sh3ll.php`

密码rebeyond

## 通达V11.x-V11.5任意用户登录获取cookie

需要用户在线，检测RELOGIN

