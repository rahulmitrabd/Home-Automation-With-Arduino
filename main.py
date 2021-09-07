import serial
from serial import Serial

ser=serial.Serial('COM13',9600, timeout=.1, xonxoff=True,)
ser.write(1)
print(ser.name)
ser.close()




