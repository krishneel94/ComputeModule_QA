import os
from textwrap import wrap
import i2c
from i2c import I2C
from args import parse
from adc import ADC
from i2c_io import _8bitIO, _16bitIO
from switch import switch_4

def main(args=None):
    sw = switch_4()
    smb = I2C()
    par = parse()
    adc = ADC()
    pers = _8bitIO()
    port = _16bitIO()
    parser = par.get_parser()
    args = parser.parse_args(args)  #inspect the command line

    err_flag = False

    if ((args.i2c0 and not args.i2c1) or (args.i2c1 and not args.i2c0)):
        try:
            data = smb.parse_func(args.data[0])
        except:
            err_flag = True
            raise
            print('Error parsing or invalid syntax, use "-h" for help')
        if not err_flag:
            if i2c.w_found and not i2c.r_found:
                try:
                    smb.write(data[0], data[1], not args.i2c0) # data[0] is data_i, data[1] is data_w
                    print('ACK')
                except IOError:
                    print('NACK...confirm you are transacting with the correct bus')
                except:
                    raise
                    print('Invalid Syntax')
            if not i2c.w_found and not i2c.r_found:
                try:
                    smb.detect(data[0], not args.i2c0)
                    print('ACK')
                except:
                    print('NACK...confirm you are transacting with the correct bus')
            if i2c.r_found and not i2c.w_found:
                try:
                    smb.read(data[0], data[2], not args.i2c0)
                except IOError:
                    print('NACK...confirm you are transacting with the correct bus')
                except:
                    raise
                    print('Invalid Syntax')
            if i2c.r_found and i2c.w_found:
                smb.write_read(data[0], data[2], data[1], not args.i2c0)

    elif args.gpio and 'getall' in args.data:
        try:
            os.system('raspi-gpio get')
        except:
            print('Invalid syntax')

    elif args.gpio and 'get' in args.data:
        try:
            os.system('raspi-gpio get ' + args.data[1])
            print('Success')
        except:
            print('Invalid syntax')

    elif args.gpio and 'set' in args.data:
        if len(args.data) == 3:
            try:
                os.system('raspi-gpio set ' + args.data[1] + ' ' + args.data[2])
                print('Success')
            except:
                print('Invalid syntax')

        if len(args.data) == 4:
            try:
                os.system('raspi-gpio set ' + args.data[1] + ' ' + args.data[2] + ' ' + args.data[3])
                print('Success')
            except:
                print('Invalid syntax')

        if len(args.data) == 5:
            try:
                os.system('raspi-gpio set ' + args.data[1] + ' ' + args.data[2] + ' ' + args.data[3] + ' ' + args.data[4])
                print('Success')
            except:
                print('Invalid syntax')
    elif args.adc:

        if args.data[0] == 'raw' and len(args.data) == 2:
            try:
                adc.raw_adc(args.data[1])
            except IOError:
                print('NACK...confirm device is powered on')
            except:
                print('Invalid syntax')
        elif args.data[0] ==  'volt' and len(args.data) == 2:
            try:
                print(adc.volt_adc(args.data[1]))
            except IOError:
                print('NACK...confirm device is powered on')
            except:
                print('Invalid syntax')
        else:
            print('Invalid syntax')
    elif args.per:
        if(args.data[0] == 'config'):
            try:
                pers.configPorts()
                print('Success')
            except IOError:
                print('NACK...confirm device is powered on')
            except:
                print('Fail!')
        elif(args.data[0] == 'arm'):
            try:
                pers.arm(args.data[1], False)
                print('Success')
            except IOError:
                print('NACK...confirm device is powered on')
            except:
                print('Invalid syntax')
        elif(args.data[0] == 'disarm'):
            try:
                pers.arm(args.data[1], True)
                print('Success')
            except IOError:
                print('NACK...confirm device is powered on')
            except:
                print('Invalid syntax')
        elif(args.data[0] == 'read'):
            try:
                pers.read_inputs()
                print('Success')
            except IOError:
                print('NACK...confirm device is powered on')
            except:
                print('Invalid syntax')
    elif args.port:
        if(args.data[0] == 'config'):
            try:
                port.configPorts()
                print('Success')
            except IOError:
                print('NACK...confirm device is powered on')
            except:
                print('Fail!')
        elif args.data[0] == 'readall':
            try:
                port.zone_readall(args.data[1])
            except IOError:
                print('NACK...confirm device is powered on')
            except:
                print('Invalid syntax')
        elif args.data[0] == 'read':
            try:
                port.zone_read(args.data[1], args.data[2])
            except IOError:
                print('NACK...confirm device is powered on')
            except:
                print('Invalid syntax')
        elif args.data[0] == 'led':
            try:
                port.led_toggle(args.data[1], args.data[2], args.data[3])
            except IOError:
                print('NACK...confirm device is powered on')
            except:
                print('Invalid syntax')
        else:
            print('Invalid syntax')
    elif args.switch:
        if args.data[0] == 'write':
            try:
                sw.ch_write(args.data[1], args.data[2], args.data[3])
            except IOError:
                print('NACK...confirm device is powered on')
            except:
                print('Invalid syntax')
        elif args.data[0] == 'readint':
            try:
                sw.read_int(args.data[1])
            except IOError:
                print('NACK...confirm device is powered on')
            except:
                print('Invalid syntax')
        elif args.data[0] == 'read':
            try:
                sw.read_dat(args.data[1], args.data[2])
            except IOError:
                print('NACK...confirm device is powered on')
            except:
                print('Invalid syntax')

    else:
        print('Invalid syntax')

if __name__ == '__main__':
    main()
