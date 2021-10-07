from ppadb.client import Client as AdbClient
import time as t
from pass_code import password as pw

# Default is "127.0.0.1" and 5037
adb = AdbClient(host="127.0.0.1", port=5037)
# print(adb.version())
devices = adb.devices()
print(devices)
device = devices[0]

url = 'https://meet.google.com/egk-oexb-kpn \n'

class android:
    def unlock(self):
        device.shell('input keyevent 26')
        t.sleep(1)
        device.shell('input touchscreen swipe 500 1200 500 500 1000')
        device.shell('input text '+pw)
        t.sleep(1)

    def lock(self):
        device.shell('input keyevent 26')

    def open_():
        device.shell('input touchscreen')
    def google_(self):
        t.sleep(1)
        device.shell('input swipe 516 1776 516 1776 100')
        t.sleep(1)
        #device.shell('input text ')
        #t.sleep(1)
        #device.shell('input keyevent 67')
        #t.sleep(1)
        device.shell('input text '+url)
        device.shell('input keyevent 66')
        t.sleep(1)
        device.shell('input swipe 400 1200 400 1200 200')
        t.sleep(5)
        device.shell('input swipe 692 1160 692 1160 200')
    def chrome(self):
        t.sleep(1)
        device.shell('input swipe 410 1027 410 1027 1000')
        t.sleep(1)
        device.shell('input text ')
        t.sleep(1)
        device.shell('input text '+url)
        device.shell('input keyevent 66')

a=android()
a.unlock()
t.sleep(1)
a.google_()
#a.chrome()

