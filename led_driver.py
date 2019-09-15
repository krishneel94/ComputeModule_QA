import os
from time import sleep
class led_drive():
    def swblink(self):
        os.system('raspi-gpio set 4 op dh')
        i = 0
        while(i != 5):
            os.system('raspi-gpio set 12 op dh')
            sleep(1)
            os.system('raspi-gpio set 12 op dl')
            sleep(1)
            i = i + 1
        os.system('raspi-gpio set 4 op dh')
    def stat1(self):
        os.system('raspi-gpio set 22 op dh')
    def stat2(self):
        os.system('raspi-gpio set 23 op dh')
