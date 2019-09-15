from i2c import I2C
smb = I2C()

class switch_4():
    def ch_write(self, zone, port, data):
        if zone == 'a':
            if port == '1':
                smb.write('0x72', '01', True) #writes 0x01 to the 4 bus switch to enable CH 1
            if port == '2':
                smb.write('0x72', '02', True)

            if port == '3':
                smb.write('0x72', '04', True)

            if port == '4':
                smb.write('0x72', '08', True)
            smb.write('0x72', data, True) # writes data to whatever CH was enabled

        if zone == 'b':
            if port == '1':
                smb.write('0x73', '01', True)

            if port == '2':
                smb.write('0x73', '02', True)

            if port == '3':
                smb.write('0x73', '04', True)

            if port == '4':
                smb.write('0x73', '08', True)
            smb.write('0x73', data, True)
    def read_dat(self, psu_addr, _bytes):
    #need to find out PSU addresses, add it as a param, a read to the slave does NOT NEED TO ACCESS THE SWITCH, merely necessary that the switch channel is enabled
        res = smb.read(hex(psu_addr), _bytes, True) 

    def read_int(self, zone):
        if zone == 'a':
            res = smb.read('0x72', '1', True) #performs a read on command reg
            res = int(res[0], 16)
            #check binary positions for ALERT
            if res and (1<<4):
                print('ZA1-Alert set')
            if res and (1<<5):
                print('ZA2-Alert set')
            if res and (1<<6):
                print('ZA3-Alert set')
            if res and (1<<7):
                print('ZA4-Alert set')
        if zone == 'b':
            res = smb.read('0x73','1', True)
            res = int(res[0], 16)
            if res and (1<<4):
                print('ZB1-Alert set')
            if res and (1<<5):
                print('ZB2-Alert set')
            if res and (1<<6):
                print('ZB3-Alert set')
            if res and (1<<7):
                print('ZB4-Alert set')



#need to still write device addr on the other side, one at a time
