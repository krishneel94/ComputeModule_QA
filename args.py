import argparse
class parse():
    def get_parser(self):
        parser = argparse.ArgumentParser(prog='RAIL Bring Up Utility', usage='%(prog)s [-i] [-j] [-g] [-h] [-a] [-u] [-s] args', formatter_class=argparse.RawTextHelpFormatter)  #create the parse object, describe what it does

        parser.add_argument('data', metavar = 'DATA', type=str, nargs = '+',
                             help='Transactional data')

        parser.add_argument('-i','--i2c0', help='''initiate i2c transaction on bus 0 (using 8 bit addresses)
-i 52wA01315       Writes 0xA0, 0x13, 0x15 to slave at 0x52
-i 52r54           Reads 54 bytes from slave at 0x52
-i 52w13r1         Writes ox13 and then issues a repeat start to perform a read of 1 byte
-i 52              Detects if a slave device exists at addr 0x52
''', action="store_true")
        parser.add_argument('-j','--i2c1', help='''initiate i2c transaction on bus 1 (using 8 bit addresses)
-j 52wA01315       Writes 0xA0, 0x13, 0x15 to slave at 0x52
-j 52r54           Reads 54 bytes from slave at 0x52
-j 52w13r1         Writes ox13 and then issues a repeat start to perform a read of 1 byte
-j 52              Detects if a slave device exists at addr 0x52
''', action="store_true")
        parser.add_argument('-g','--gpio', help= '''GPIO checking and control
getall -g          Prints state of all GPIOs one per line
get 20 -g          Prints state of GPIO20
set 20 a5 -g       Set GPIO20 to ALT5 function (GPCLK0)
set 20 pu -g       Enable GPIO20 ~50k in-pad pull up
set 20 pd -g       Enable GPIO20 ~50k in-pad pull down
set 20 op -g       Set GPIO20 to be an output
set 20 dl -g       Set GPIO20 to output low\n(must already be set as an output)
set 20 ip pd -g    Set GPIO20 to input with pull down
set 35 a0 pu -g    Set GPIO35 to ALT0 function\n(SPI_CE1_N) with pull up
set 20 op pn dh -g Set GPIO20 to ouput with no pull and\ndriving high
''',action="store_true")
        parser.add_argument('-a', '--adc', help='''Get ADC Data
-a raw hot         Get raw ADC data from hot side thermistor
-a raw cold        Get raw ADC data from cold side thermistor
-a raw flow        Get raw ADC data from flow sensor
-a raw temp        Get raw ADC data from temperature sensor
-a volt hot        Get ADC voltage from hot side thermistor
-a volt cold       Get ADC voltage data from cold side thermistor
-a volt flow       Get ADC voltage from flow sensor
-a volt temp       Get ADC voltage from temperature sensor
''', action="store_true")
        parser.add_argument('-p', '--per', help='''8 bit (persistent) I/O
-p config          Config I/O ports
-p arm a           Set 'ZA-Armed'
-p arm b           Set 'ZB-Armed'
''', action="store_true")
        parser.add_argument('-u', '--port', help='''16 bit I/O
-u config          Config I/O ports
-u readall a       Read all INOK and PWROK from zone A
-u read a 1        Read INOK and PWROK from zone A port 1
-u led a 1 2       Toggle LED 2 in zone A port 1
''', action="store_true")
        parser.add_argument('-s', '--switch', help='''4CH I2C Switch
-s write a 1 0010  Write 0x00 and 0x10 to zone A port 1
-s readint a       Check if any alarm in zone A is set
-s read 0x52 1     Read the data from this addr
''', action="store_true")
        return parser
#add interrupt poll
