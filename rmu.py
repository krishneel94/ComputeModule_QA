from i2c import I2C
from switch import switch_4
from i2c_io import _16bitIO, _8bitIO
from led_driver import led_drive
from adc import ADC
import os
led = led_drive()
smb = I2C()
sw = switch_4()
port = _16bitIO()
per = _8bitIO()
adc = ADC()
import time
import argparse
class parse():
    def get_parser(self):
        parser = argparse.ArgumentParser(prog='RAIL Manufacturing Utility', usage='%(prog)s [-t] args', formatter_class=argparse.RawTextHelpFormatter)  #create the parse object, describe what it does

        parser.add_argument('data', metavar = 'DATA', type=str, nargs = '+',
                             help='Transactional data')
        parser.add_argument('-t','--test', help='-t start FF Starts test and sends 0xFF to I2C Switch', action="store_true")
        return parser

class RMU():
    def test(self,data):
        print('Testing INOK, and PWROK pins in Zone A')
        print('ZA1 and ZA3 set as outputs, ZA2 and ZA4 set as inputs')
        smb.write('0x74', '06CC00', False)
        smb.write('0x74', '0223', False)
        res = smb.write_read('0x74', '1', '00', False)

        if res[0] == '0xaf':
            print('Pass!')
        else:
            print('FAIL')
        smb.write('0x74', '0233', False)
        res = smb.write_read('0x74', '1', '00', False)
        if res[0] == '0xff':
            print('Pass!')
        else:
            print('FAIL')

        print('ZA2 and ZA4 set as outputs, ZA1 and ZA3 set as inputs')
        smb.write('0x74', '063300', False)
        smb.write('0x74', '0288', False)
        res = smb.write_read('0x74', '1', '00', False)
        if res[0] == '0xaa':
            print('Pass!')
        else:
            print('FAIL')

        smb.write('0x74', '0244', False)
        res = smb.write_read('0x74', '1', '00', False)
        if res[0] == '0x55':
            print('Pass!')
        else:
            print('FAIL')

        print('Testing INOK, and PWROK pins in Zone B')
        print('ZB1 and ZB3 set as outputs, ZB2 and ZB4 set as inputs')
        smb.write('0x75', '06CC00', False)
        smb.write('0x75', '0223', False)
        res = smb.write_read('0x75', '1', '00', False)
        if res[0] == '0xaf':
            print('Pass!')
        else:
            print('FAIL')
        smb.write('0x75', '0233', False)
        res = smb.write_read('0x75', '1', '00', False)
        if res[0] == '0xff':
            print('Pass!')
        else:
            print('FAIL')

        print('ZB2 and ZB4 set as outputs, ZB1 and ZB3 set as inputs')
        smb.write('0x75', '063300', False)
        smb.write('0x75', '0288', False)
        res = smb.write_read('0x75', '1', '00', False)
        if res[0] == '0xaa':
            print('Pass!')
        else:
            print('FAIL')
        smb.write('0x75', '0244', False)
        res = smb.write_read('0x75', '1', '00', False)
        if res[0] == '0x55':
            print('Pass!')
        else:
            print('FAIL')

#add i2c checking
        print('Testing JACK LEDs')
        port.led_toggle('all', '0', '0')
        time.sleep(1)
        port.led_toggle('none', '0', '0')
        time.sleep(1)
        port.led_toggle('all', '0', '0')
        time.sleep(1)
        port.led_toggle('none', '0', '0')
        time.sleep(1)
        port.led_toggle('all', '0', '0')
        time.sleep(1)
        port.led_toggle('none', '0', '0')
        print('Taking over HW Blink')
        led.swblink()
        print('Trying stat1')
        led.stat1()
        print('Trying stat2')
        led.stat2()
        
        print('Testing ADC, make sure to check these values are correct!!!')
        time.sleep(2)
        print('Hot side thermistor...')
        print(adc.volt_adc('hot'))
        print('Cold side thermistor...')
        print(adc.volt_adc('cold'))
        print('NTC...')
        print(adc.volt_adc('temp'))
        print('Flow...')
        print(adc.volt_adc('flow'))
        print('Testing Leak Sensor...')
        answer = 0
        answer = input('Leave the switch open and press enter to continue...the "level" should be 0')
        os.system('sudo raspi-gpio get 36')
        answer = input('Press the switch closed and press enter to continue...the "level" should be 1')
        os.system('sudo raspi-gpio get 36')
        per.configPorts()
        per.arm('a', True)
        per.arm('b', True)
        print('Connect EPO tester now and press enter continue')
        answer = input('Ready..?')
        per.arm('a', False)
        print('Check PSON for A')
        answer = input('Ready for B? Press enter to continue...')
        per.arm('b', False)
        print('Check PSON for B')
        print('Before sign off !!! >> Make sure the MAC address is flashed AND power transistions smoothly from POE to AUX!!')
#ask user to verify there is ethernet connection
#check that MAC is flashed
        answer = input('End of test...press enter to exit')
        

def main(args=None):
    par = parse()
    parser = par.get_parser()
    args = parser.parse_args(args)  #inspect the command line
    rmu = RMU()
    if args.test:
        try:
            rmu.test(args.data[1])
        except IOError:
            print('Nack...confirm device is powered on')
        except:
            raise


if __name__ == '__main__':
    main()
