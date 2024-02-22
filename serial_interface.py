import serial
import time


def serial_read():
    reply = b""
    while ser.in_waiting:
        reply += ser.read(ser.in_waiting)
        time.sleep(0.1)
    return reply


def serial_write(string):
    ser.write(string + b"\r\n")
    time.sleep(0.1)
    return serial_read().decode()


# Liam's port:
portL = "/dev/cu.usbmodem3356396133381"
# Jesse's port:
portJ = "COM13"

ser = serial.Serial(
    port=portJ,  ## <----------- REPLACE with your SPIKE's port from!!!##
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
)

ser.isOpen()
ser.write(b"\x03")
print(serial_read())
