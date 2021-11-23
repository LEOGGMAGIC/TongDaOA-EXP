import os
import time
import requests
from pyfiglet import Figlet
from rich.console import Console
from Plugins import TongDaOA_getVersion
from Plugins import TongDaOA_emptyPwd
from Plugins import TongDaOA_113fileInclude
from Plugins import TongDaOA_113fileUpload
from Plugins import TongDaOA_114getSession
from Plugins import TongDaOA_115sqlInjection
from Plugins import TongDaOA_116deleteFile
from Plugins import TongDaOA_117relogin
from Plugins import TongDaOA_117sqlInjection
from Plugins import TongDaOA_118useriniUpload
from Plugins import TongDaOA_119sqlInjection

END = '\033[0m'
console = Console()

def main():
    host = input("请输入目标URL地址：")
    TongDaOA_getVersion.run(host)
    TongDaOA_emptyPwd.run(host)
    TongDaOA_113fileInclude.run(host)
    TongDaOA_113fileUpload.run(host)
    TongDaOA_114getSession.run(host)
    TongDaOA_115sqlInjection.run(host)
    TongDaOA_116deleteFile.run(host)
    TongDaOA_117relogin.run(host)
    TongDaOA_117sqlInjection.run(host)
    TongDaOA_118useriniUpload.run(host)
    TongDaOA_119sqlInjection.run(host)
    

if __name__ == '__main__':
    console.print(Figlet(font='slant').renderText('TongDaOA-EXP'), style='magenta') #定义宽字体且为紫色
    console.print('         Author: LEOGGMAGIC    \n', style='red')
    main()
