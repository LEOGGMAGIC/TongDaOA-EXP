# 通达OA系列检测EXP

通达OA V11全版本漏洞检测

检测模块集成在Plugins文件夹内

稍微改了一下这位大佬的exp`https://github.com/kitezzzGrim/tongda-exp`

代码写的有点💩，有新的检测模块和意见欢迎交流学习~

## Plugins文件夹

使用方法（python3）

```
python TongDaOA.py
```

根据提示输入URL地址：`http://xxx.xxx.xxx.xxx:xxxx/`，注意URL最后带上`/`

一键检测，测试案例如下（通达V11.2）

![](pic/1.gif)

### 获取版本信息

检测`inc/expired.php`是否存在版本信息泄露

### 空口令登录

使用空口令尝试登陆

### 通达<11.3任意文件包含漏洞

检测是否存在文件包含漏洞

如果存在尝试读取`general/../../mysql5/my.ini`

### 通达<11.3文件上传+文件包含getshell

先检测是否存在文件包含漏洞，如果存在直接上🐎

存在漏洞会在这个目录生成冰蝎马`ispirit/interface/sh3ll.php`

密码rebeyond

### 通达<V11.4任意用户cookie获取漏洞

控制UID=1来获取admin的cookie

### 通达<V11.7任意在线用户登录漏洞

需要用户在线，检测RELOGIN

### 通达<V11.8上传.user.ini文件包含漏洞getshell

需填入cookie，输入PHPSESSID=XXXX

存在漏洞会在这个目录上传冰蝎马`general/reportshop/workshop/report/attachment-remark/form.inc.php`

密码rebeyond

<<<<<<< HEAD

## Danger文件夹

### 通达V11.5后台SQL注入漏洞

需要一个普通账户的用户名/密码

GET方法测试`general/appbuilder/web/report/repdetail/edit?link_type=false&slot={}&id=2`

测试id是否存在注入

```
python TongDaOA_115sqlInjection.py
```

输入URL，用户名/密码，如果存在漏洞，把请求包放入sqlmap跑

### 通达V11.6任意文件删除漏洞getshell

删除`auth.inc.php`认证文件，有风险请在授权状态下使用（任意删除文件只在11.6有）

在danger文件夹内运行

```
python TongDaOA_116deleteFile.py
```

### 通达V11.7后台SQL注入&新增数据库用户写webshell

此漏洞需要一个普通账户的用户名/密码

在danger文件夹内运行

```
python TongDaOA_117sqlInjection.py
```

根据提示输入URL地址，以及用户名/密码

会向数据中新增账户并提权`abc123:abc123@abc123`

以下是获取数据库权限后的操作，举个例子：

```
# 通过数据库写webshell方法有很多:
# select @@basedir可以查询绝对路径：C:\TDOA11.7\mysql5\
# 那通达OA的web目录就是C:/TDOA11.7/webroot
# select @@basedir
# set global general_log='on';
# SET global general_log_file='c:/TDOA11.7/webroot/aaa.php';
# SELECT '一句话木马';
```

### 通达<V11.9 后台SQL时间盲注漏洞

此漏洞需要cookie，请先运行TongDaOA.py通过其他漏洞获取cookie

在danger文件夹内运行

```
python TongDaOA_119sqlInjection.py
```

测试有漏洞后放到sqlmap跑
