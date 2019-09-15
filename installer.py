import os
import time
import subprocess
#os.system('sudo apt-get install raspi-gpio')
#os.system('sudo pip3 install smbus2')
proc = subprocess.call("sudo apt-get install raspi-gpio", shell = True)
proc = subprocess.call("sudo pip3 install smbus2", shell = True)
os.system('echo "#Added by Loco" | sudo tee /boot/config.txt -a')
os.system('echo "dtparam=i2c0=on" | sudo tee /boot/config.txt -a')
os.system('echo "gpio=13=op,dh" | sudo tee /boot/config.txt -a')
os.system('echo "gpio=36=ip" | sudo tee /boot/config.txt -a')