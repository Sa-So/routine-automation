from ppadb.client import Client as AdbClient
import time as t
from pass_code import password as pw
from mlh_lhd import event_url
#event_url = 'https://organize.mlh.io/participants/events/7574-lhd-learn-cup-levitation';
# Default is "127.0.0.1" and 5037
adb = AdbClient(host="127.0.0.1", port=5037)
# print(adb.version())
devices = adb.devices()
print(devices)
device = devices[0]

urli = 'https://meet.google.com/egk-oexb-kpn \n'


class android:
    def unlock(self):
        device.shell('input keyevent 26')
        t.sleep(1)
        device.shell('input swipe 530 2364 530 2364 200')
        #t.sleep(1)
        device.shell('input touchscreen swipe 500 1200 500 500 1000')
        device.shell('input text '+pw)
        device.shell('input swipe 535 2342 535 2342 150')
        t.sleep(1)

    def lock(self):
        device.shell('input keyevent 26')

    def open_():
        device.shell('input touchscreen')

    def google_(self,url):
        t.sleep(1)
        device.shell('input swipe 516 1776 516 1776 100')
        t.sleep(1)
        #device.shell('input text ')
        # t.sleep(1)
        #device.shell('input keyevent 67')
        # t.sleep(1)
        device.shell('input text '+url)
        device.shell('input keyevent 66')
        t.sleep(1)
        device.shell('input swipe 400 1200 400 1200 200')
        t.sleep(5)
        device.shell('input swipe 692 1190 692 1190 200')
        t.sleep(3)
        # 849 1343
        device.shell('input swipe 849 1343 849 1343 200')
        t.sleep(2)
        device.shell('input keyevent 26')
        t.sleep(5)


    def chrome(self):
        t.sleep(1)
        device.shell('input swipe 410 1027 410 1027 1000')
        t.sleep(1)
        device.shell('input text ')
        t.sleep(1)
        device.shell('input text '+urli)
        device.shell('input keyevent 66')

    def join_mlh(self):
        t.sleep(1)
        device.shell('input swipe 516 1776 516 1776 100')
        t.sleep(1)
        device.shell('input text ' + event_url)
        device.shell('input keyevent 66')
        t.sleep(15)
        device.shell('input swipe 247 1512 247 1512 120')
        t.sleep(10)
        device.shell('input swipe 530 1535 530 1535 120')

#a = android()
#a.unlock()
#t.sleep(1)
#a.join_mlh()
# a.google_()
# a.chrome()
