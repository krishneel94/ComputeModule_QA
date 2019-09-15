from i2c import I2C
smb = I2C()
class ADC():
    def raw_adc(self, ch):

        if ch == 'hot':
            smb.write('0x48', '00C8', False)
            smb.read('0x48', '1', False)
            res0 = smb.write_read('0x48', '1', '02', False)
            res1 = smb.write_read('0x48', '1', '03', False)

        if ch == 'cold':
            smb.write('0x48', '01C8', False)
            smb.read('0x48', '1', False)
            res0 = smb.write_read('0x48', '1', '04', False)
            res1 = smb.write_read('0x48', '1', '05', False)
        if ch == 'flow':
            smb.write('0x48', '02C8', False)
            smb.read('0x48', '1', False)
            res0 = smb.write_read('0x48', '1', '06', False)
            res1 = smb.write_read('0x48', '1', '07', False)

        if ch == 'temp':
            smb.write('0x48', '03C8', False)
            smb.read('0x48', '1', False)
            res0 = smb.write_read('0x48', '1', '08', False)
            res1 = smb.write_read('0x48', '1', '09', False)

        res0 = int(res0[0] , 16)
        res1 = int(res1[0] , 16)
        res1 = res1 >> 4
        res1 = (res0 << 4) + res1
        res1 = int(hex(res1), 16)
        return res1

    def volt_adc(self, ch):
        res = self.raw_adc(ch)
        res = res * (5/4096)
        return res
#TODO
#Create a function that will convert VOLTAGE to a meaningful value
