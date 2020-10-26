# This program opens a serial port, sends a read command, checks the response and then closes the port

import serial
import binascii
import codecs

ser = serial.Serial()
ser.baudrate = 115200
ser.port = '/dev/ttyUSB0'
ser.parity='N'
ser.stopbits=1 
ser.timeout=1
ser.xonxoff=0
ser.rtscts=1
ser.bytesize=8

ser.open()
clear = b'0000'    
print(codecs.encode(clear,"hex")) # Display the bytes that will be sent in hex
ser.write(clear)

command = b'RD' # This syntax says treat this as ascii and convert it to bytes
N = b'\x01'      # This syntax says treat this as bytes

message = command + N

print(message)

ser.write(message)
print(ser.read(2))

ser.close()