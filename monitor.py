import serial

addr = '/dev/ttyACM0'
baudrate = 9600
timeout = 1

dev = serial.Serial()

dev.baudrate = baudrate
dev.port = addr
dev.timeout = timeout
dev.open()

while True:
    print(dev.readline())

dev.close()
