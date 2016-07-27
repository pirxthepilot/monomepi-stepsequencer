from arduinopi import Arduino
import binascii


class Servo(Arduino):

    def __init__(self, serial_port):
        super(Servo, self).__init__(serial_port)

    def open_servo(self):
        self.open()

    def move(self, servodata):
        self.write(tobytes(servodata))


# FUNCTIONS

def tobytes(b1):
    b1_hex = format(int(b1), '02x')
    print b1_hex
    return binascii.unhexlify(b1_hex)
