import serial
import time


class Arduino(object):

    def __init__(self, serial_port, baud=115200):
        self.serial_port = serial_port
        self.baud = baud

    def open(self):
        self.ser = serial.Serial(self.serial_port, self.baud)
        print "Init Arduino serial port..",
        time.sleep(2)
        print "Done!"

    def close(self):
        print "Closing Arduino serial port.."
        self.ser.close()

    def write(self, message):
        self.ser.write(str(message))
