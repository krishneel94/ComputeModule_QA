from smbus2 import SMBus, i2c_msg
from textwrap import wrap
w_found = False
r_found = False
bus0 = SMBus(0)
bus1 = SMBus(1)
class I2C():

    def detect(self, addr, bus):
        if bus == False:
            bus0.read_byte(int(addr, 16))
        elif bus == True:
            bus1.read_byte(int(addr, 16))

    def write_read(self, addr, size, value, bus):
        if bus == False:
            value = wrap(value, 2)
            for x in range(len(value)):
                value[x] = int(value[x], 16)
            write = i2c_msg.write(int(addr, 16), value)
            read = i2c_msg.read(int(addr, 16), int(size,10))
            bus0.i2c_rdwr(write, read)
            dat =  list(read)
            for x in range(len(dat)):
                dat[x] = hex(dat[x])
            print(dat)


        elif bus == True:
            value = wrap(value, 2)
            for x in range(len(value)):
                value[x] = int(value[x], 16)
            write = i2c_msg.write(int(addr, 16), value)
            read = i2c_msg.read(int(addr, 16), int(size,10))
            bus1.i2c_rdwr(write, read)
            dat =  list(read)
            for x in range(len(dat)):
                dat[x] = hex(dat[x])
            print(dat)
        return dat

    def read(self, addr, size, bus):
        if bus == False:
            read = i2c_msg.read(int(addr, 16), int(size,10))
            bus0.i2c_rdwr(read)
            dat =  list(read)
            for x in range(len(dat)):
                dat[x] = hex(dat[x])
            print(dat)


        elif bus == True:
            read = i2c_msg.read(int(addr, 16), int(size,10))
            bus1.i2c_rdwr(read)
            dat =  list(read)
            for x in range(len(dat)):
                dat[x] = hex(dat[x])
            print(dat)
        return dat

    def write(self, addr, value, bus):
        value = wrap(value, 2)
        if bus == False:
            for x in range(len(value)):
                value[x] = int(value[x], 16)
            write = i2c_msg.write(int(addr, 16), value)
            bus0.i2c_rdwr(write)

        elif bus == True:
            for x in range(len(value)):
                value[x] = int(value[x], 16)
            write = i2c_msg.write(int(addr, 16), value)
            bus1.i2c_rdwr(write)

        return value[0]

    def parse_func(self, argument_dat):
        x = 0
        global w_found
        global r_found
        data_i = ''
        data_w = ''
        data_r = ''
        data_b = ''
        data = []
        data_i = data_i + argument_dat[x]
        data_i = data_i + argument_dat[x + 1]
        data_i = int(data_i, 16)
        data_i = data_i >> 1
        data_i = hex(data_i)
        if len(argument_dat) > 2:
            argument_dat = argument_dat[2:]
            if argument_dat[0] == 'r':
                r_found = True
                x = 1
                while x != len(argument_dat):
                    data_r = data_r + argument_dat[x]
                    x = x + 1
            x = 1
            if 'w' in argument_dat and 'r' in argument_dat:
                w_found = True
                while x != len(argument_dat):
                    if not r_found:
                        if argument_dat[x] == 'r':
                            r_found = True
                            x = x + 1
                        else:
                            data_w = data_w + argument_dat[x]
                            x = x + 1
                    if r_found:
                        data_r = data_r + argument_dat[x]
                        x = x + 1
            elif 'w' in argument_dat and 'r' not in argument_dat:
                w_found = True
                while x != len(argument_dat):
                    if not r_found:
                        if argument_dat[x] == 'r':
                            r_found = True
                            x = x + 1
                        else:
                            data_w = data_w + argument_dat[x]
                            x = x + 1
                    if r_found:
                        data_r = data_r + argument_dat[x]
                        x = x + 1
        data.append([data_i, data_w, data_r])
        data = data[0]
        return data
