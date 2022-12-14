import smbus
import time

recieved_address = 0x20

bus = smbus.SMBus(1)


def Light(addr=BH1750_sensor):
    address = bus.read_i2c_block_data(BH1750_sensor, recieved_address)
    value = Light_intensity(address)
    return Light_intensity(address)


def Light_intensity(address):
    return ((address[1] + (256 * address[0])) / 1.2)


def message():
    while True:
        intensity = Light()
        print(intensity)
        if (intensity >= 500):
            print("extra brightness")
        elif (intensity > 220 and intensity < 500):
            print("brightness")
        elif (intensity > 50 and intensity < 200):
            print("Medium brightness")
        elif (intensity > 50 and intensity < 20):
            print("Dark")
        elif (intensity < 20):
            print("very drak")
        time.sleep(1)


message()