import serial
import time
import sys


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
    port=portL,  ## <----------- REPLACE with your SPIKE's port from!!!##
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
)

# BUG catch serial not open error
ser.isOpen()
ser.write(b"\x03")
print(serial_read())


def test_serial():

    test = """import motor
from hub import port
import time
i = 0
while i < 1000:
print("hello world")
# motor.run_for_degrees(port.A,-360, 75)
# motor.run_for_degrees(port.B,360, 75)
time.sleep(.5)
i = i + 1"""

    #     test = \
    # '''for i in range(10):
    #     print("hello world")'''

    test = """import motor
from hub import port
import runloop
import time

async def main():
print("hello world")
await motor.run_for_degrees(port.A,-360, 75)
await motor.run_for_degrees(port.B,360, 75)
time.sleep(3)
await motor.run_for_degrees(port.A,-360, 75)
await motor.run_for_degrees(port.B,360, 75)



runloop.run(main())
"""

    # reply = serial_write(bytes("\x05", 'utf-8'))
    # print(reply)

    test = test.replace("\n", "\r\n")
    reply = serial_write(bytes(test, "utf-8"))
    print(reply)
    time.sleep(1)
    # reply = serial_write(bytes("\x03", 'utf-8'))
    print(reply)

    sys.exit()
