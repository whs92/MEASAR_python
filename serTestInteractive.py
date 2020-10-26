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

# Open and clear the port
ser.open()
clear = b'0000'    
ser.write(clear)

N = b'\x01'      # This syntax says treat this as bytes

# Get the instruction from the user
instruction = input("Enter the Instruction String: ")

while instruction != "X" :

    if "W" in instruction :
        value = input("Enter the Value Hex: ")
        value = bytearray.fromhex(value)
    else : 
        value = b''
   
    
    command = bytes(instruction, "ascii")
    message = command + N + value
    print(message)
    
    ser.write(message)
    print(ser.read(3))
    
    # Get the instruction from the user
    instruction = input("Enter the Instruction String: ")

ser.close()