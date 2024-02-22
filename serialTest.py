import serial.tools.list_ports

ser = None


def serial_ports():
    result = []
    ports = serial.tools.list_ports.comports()
    for port, desc, hwid in sorted(ports):
        comm = "{}: {}".format(port, desc)
        result.append(comm)
    return result


print(serial_ports())
