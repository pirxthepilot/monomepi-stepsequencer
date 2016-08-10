from monomepi128 import Arduino
import binascii


class Servo(Arduino):

    def __init__(self, serial_port):
        super(Servo, self).__init__(serial_port)

    def open_servo(self):
        self.open()

    def move(self, servodata):
        """Now accepts hex, not int"""
        self.write(binascii.unhexlify(servodata))
