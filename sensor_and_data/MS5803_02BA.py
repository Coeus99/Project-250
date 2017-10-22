import smbus
import time

def get_temp_pres():
        bus = smbus.SMBus(1)

        bus.write_byte(0x76, 0x1E)

        time.sleep(0.5)

        data = bus.read_i2c_block_data(0x76, 0xA2, 2)
        C1 = data[0] * 256 + data[1]

        data = bus.read_i2c_block_data(0x76, 0xA4, 2)
        C2 = data[0] * 256 + data[1]

        data = bus.read_i2c_block_data(0x76, 0xA6, 2)
        C3 = data[0] * 256 + data[1]

        data = bus.read_i2c_block_data(0x76, 0xA8, 2)
        C4 = data[0] * 256 + data[1]

        data = bus.read_i2c_block_data(0x76, 0xAA, 2)
        C5 = data[0] * 256 + data[1]

        data = bus.read_i2c_block_data(0x76, 0xAC, 2)
        C6 = data[0] * 256 + data[1]

        bus.write_byte(0x76, 0x40)

        time.sleep(0.5)

        value = bus.read_i2c_block_data(0x76, 0x00, 3)
        D1 = value[0] * 65536 + value[1] * 256 + value[2]

        bus.write_byte(0x76, 0x50)

        time.sleep(0.5)

        value = bus.read_i2c_block_data(0x76, 0x00, 3)
        D2 = value[0] * 65536 + value[1] * 256 + value[2]

        dT = D2 - C5 * 256
        TEMP = 2000 + dT * C6 / 8388608
        OFF = C2 * 131072 + (C4 * dT) / 64
        SENS = C1 * 65536 + (C3 * dT ) / 128
        T2 = 0
        OFF2 = 0
        SENS2 = 0

        if TEMP >= 2000 :
                T2 = 0
                OFF2 = 0
                SENS2 = 0
        elif TEMP < 2000 :
                T2 = (dT * dT) / 2147483648
                OFF2= 61 * ((TEMP - 2000) * (TEMP - 2000)) / 16
                SENS2= 2 * ((TEMP - 2000) * (TEMP - 2000))
                if TEMP < -1500 :
                        OFF2 = OFF2 + 20 * ((TEMP + 1500) * (TEMP + 1500))
                        SENS2 = SENS2 + 12 * ((TEMP + 1500) * (TEMP +1500))

        TEMP = TEMP - T2
        OFF = OFF - OFF2
        SENS = SENS - SENS2
        pressure = ((((D1 * SENS) / 2097152) - OFF) / 32768.0) / 100.0
        pPressure = pressure * 100
        cTemp = TEMP / 100.0
        fTemp = cTemp * 1.8 + 32

        return [cTemp, pPressure]
