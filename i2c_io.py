from i2c import I2C
smb = I2C()

class _8bitIO():
    def configPorts(self):
        smb.write('0x73', '03FC', False) #write to config register 1111 1011. All are set as input except ZA and ZB Armed
    def arm(self, zone, disarm):
        if disarm == True:
            if zone == 'a':
                res = smb.write_read('0x73', '1', '00', False)
                res = int(res[0], 16)
                if (1 << 1) and res:
                    smb.write('0x73', '0103', False) #writes a 1 to pin 0 while pin 1 is set
                if not ((1 << 1) and res):
                    smb.write('0x73', '0101', False) #writes a 1 to pin 0 while pin 1 is not set
                smb.read('0x73', '1', False)
            elif zone== 'b':
                res = smb.write_read('0x73', '1', '00', False)
                res = int(res[0], 16)
                if (1 << 0) and res:
                    smb.write('0x73', '0103', False) #writes a 1 to pin 1 while pin 1 is set
                if not ((1 << 0) and res):
                    smb.write('0x73', '0102', False) #writes a 1 to pin 1 while pin 0 is not set
                smb.read('0x73', '1', False)
        if disarm == False:
            if zone == 'a':
                res = smb.write_read('0x73', '1', '00', False)
                res = int(res[0], 16)
                if (1 << 1) and res:
                    smb.write('0x73', '0102', False) #turns pin 0 off keeps pin 1 on
                if not ((1 << 1) and res):
                    smb.write('0x73', '0100', False) #turns both off
                smb.read('0x73', '1', False)
            elif zone== 'b':
                res = smb.write_read('0x73', '1', '00', False)
                res = int(res[0], 16)
                if (1 << 0) and res:
                    smb.write('0x73', '0101', False)
                if not ((1 << 0) and res):
                    smb.write('0x73', '0100', False)
                smb.read('0x73', '1', False)					
    def read_inputs(self):
        res = smb.write_read('0x73', '1', '00', False)
        res = int(res[0], 16)
        if res and (1 << 2):
            print('ZA-PSON is set!')
        elif not ((1 << 2) and res):
            print('ZA-PSON is not set!')
        if res and (1 << 3):
            print('ZB-PSON is set!')
        elif not ((1 << 3) and res):
            print('ZB-PSON is not set!')
        if res and (1 << 4):
            print('ZA-PWRBTN is set!')
        elif not (res and (1 << 4)):
            print('ZA-PWRBTN is not set!')
        if res and (1 << 5):
            print('ZB-PWRBTN is set!')
        elif not (res and (1 << 5)):
            print('ZB-PWRBTN is not set!')
class _16bitIO():
    def configPorts(self):
        smb.write('0x74', '06FF00', False) # LS Byte is set for all inputs, MS byte is set for all outputs
        smb.write('0x75', '06FF00', False) # LS Byte is set for all inputs, MS byte is set for all outputs
    def zone_readall(self, zone):
        if zone == 'a':
            res = smb.write_read('0x74', '1', '00', False)
            if res[0] == '0xff':
                print('All Zone A INOK and PWROK')
            else:
                print('Not all OK, check ports')
        if zone == 'b':
            res = smb.write_read('0x75', '1', '00', False)
            if res[0] == '0xff':
                print('All Zone B INOK and PWROK')
            else:
                print('Not all OK, check ports individually')
    def zone_read(self, zone, port):
    #put a conditional in the print
        if zone == 'a':
            res = smb.write_read('0x74', '1', '00', False)
            res = int(res[0], 16)
            if port == '1':
                if res and (1 << 1):
                    print('ZA1 PWROK...CHECK!')
                elif not (res and (1 << 1)):
                    print('ZA1 PWROK...NOT GOOD')
                if res and (1 << 0):
                    print('ZA1 INOK...CHECK!')
                elif not (res and (1 << 0)):
                    print('ZA1 INOK...NOT GOOD')
            if port == '2':
                if res and (1 << 3):
                    print('ZA2 PWROK...CHECK!')
                elif not (res and (1 << 3)):
                    print('ZA2 PWROK...NOT GOOD')
                if res and (1 << 2):
                    print('ZA2 INOK...CHECK!')
                elif not (res and (1 << 2)):
                    print('ZA2 INOK...NOT GOOD')
            if port == '3':
                if (res and (1 << 5)):
                    print('ZA3 PWROK...CHECK!')
                elif not (res and (1 << 3)):
                    print('ZA3 PWROK...NOT GOOD')
                if (res and (1 << 4)):
                    print('ZA3 INOK...CHECK!')
                elif not (res and (1 << 4)):
                    print('ZA3 INOK...NOT GOOD')
            if port == '4':
                if (res and (1 << 7)):
                    print('ZA4 PWROK...CHECK!')
                elif not (res and (1 << 7)):
                    print('ZA4 PWROK...NOT GOOD')
                if (res and (1 << 6)):
                    print('ZA4 INOK...CHECK!')
                elif not (res and (1 << 6)):
                    print('ZA4 INOK...NOT GOOD')
        if zone == 'b':
            res = smb.write_read('0x74', '1', '00', False)
            res = int(res[0], 16)
            if port == '1':
                if res and (1 << 1):
                    print('ZB1 PWROK...CHECK!')
                elif not (res and (1 << 1)):
                    print('ZB1 PWROK...NOT GOOD')
                if res and (1 << 0):
                    print('ZB1 INOK...CHECK!')
                elif not (res and (1 << 0)):
                    print('ZB1 INOK...NOT GOOD')
            if port == '2':
                if res and (1 << 3):
                    print('ZB2 PWROK...CHECK!')
                elif not (res and (1 << 3)):
                    print('ZB2 PWROK...NOT GOOD')
                if res and (1 << 2):
                    print('ZB2 INOK...CHECK!')
                elif not (res and (1 << 2)):
                    print('ZB2 INOK...NOT GOOD')
            if port == '3':
                if (res and (1 << 5)):
                    print('ZB3 PWROK...CHECK!')
                elif not (res and (1 << 3)):
                    print('ZB3 PWROK...NOT GOOD')
                if (res and (1 << 4)):
                    print('ZB3 INOK...CHECK!')
                elif not (res and (1 << 4)):
                    print('ZB3 INOK...NOT GOOD')
            if port == '4':
                if (res and (1 << 7)):
                    print('ZB4 PWROK...CHECK!')
                elif not (res and (1 << 7)):
                    print('ZB4 PWROK...NOT GOOD')
                if (res and (1 << 6)):
                    print('ZB4 INOK...CHECK!')
                elif not (res and (1 << 6)):
                    print('ZB4 INOK...NOT GOOD')

    def led_toggle(self, zone, port, led):
    #add read, modify, write
        if zone == 'a':
            if port == '1' and led == '1':
                smb.write('0x74', '03FE', False)
            if port == '1' and led == '2':
                smb.write('0x74', '03FD', False)
            if port == '2' and led == '1':
                smb.write('0x74', '03FB', False)
            if port == '2' and led == '2':
                smb.write('0x74', '03F7', False)
            if port == '3' and led == '1':
                smb.write('0x74', '03EF', False)
            if port == '3' and led == '2':
                smb.write('0x74', '03DF', False)
            if port == '4' and led == '1':
                smb.write('0x74', '03BF', False)
            if port == '4' and led == '2':
                smb.write('0x74', '037F', False)
        if zone == 'b':
            if port == '1' and led == '1':
                smb.write('0x75', '03FE', False)
            if port == '1' and led == '2':
                smb.write('0x75', '03FD', False)
            if port == '2' and led == '1':
                smb.write('0x75', '03FB', False)
            if port == '2' and led == '2':
                smb.write('0x75', '03F7', False)
            if port == '3' and led == '1':
                smb.write('0x75', '03EF', False)
            if port == '3' and led == '2':
                smb.write('0x75', '03DF', False)
            if port == '4' and led == '1':
                smb.write('0x75', '03BF', False)
            if port == '4' and led == '2':
                smb.write('0x75', '037F', False)
        if zone == 'all':
            smb.write('0x74', '0300', False)
            smb.write('0x75', '0300', False)
        if zone == 'none':
            smb.write('0x74', '03FF', False)
            smb.write('0x75', '03FF', False)
