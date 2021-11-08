import os
import threading
import queue
import time
from Plugins import TongDaOA_getVersion
from Plugins import TongDaOA_unauth

Vuls = []
host = 'http://192.168.32.129:8081'
QeueWork = queue.Queue(50)
threads = []
exitFlag = 0
PluginsNum = 0


class Check(threading.Thread):
    def __init__(self, VulName, QeueWork):
        threading.Thread.__init__(self)
        self.VulName = VulName
        self.QeueWork = QeueWork

    def run(self):
        while not self.QeueWork.empty():
            target = self.QeueWork.get()
            self.detection(target)

    def detection(self, VulName):
        eval(VulName).run(host)


def GetPlugins():
    global PluginsNum
    for i in os.listdir('Plugins'):
        if i[-2:] == 'py':
            i = i.replace('.py', '')
            PluginsNum = PluginsNum + 1
            Vuls.append(i)
        else:
            continue
    for vul in Vuls:
        QeueWork.put(vul)


def main():
    GetPlugins()
    for vul in Vuls:
        thread = Check(vul, QeueWork)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


if __name__ == '__main__':
    main()