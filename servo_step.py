from arduinopi import Arduino
import binascii


class Servo(Arduino):

    def __init__(self, serial_port):
        super(Servo, self).__init__(serial_port)
        self.i = 0

    def open_servo(self):
        self.open()

    def move(self, servo):
        self.write(tobytes(servo))
        print str(self.i) + "write " + servo
        self.i += 1

    def reset(self, servo):
        self.move(servo)


# FUNCTIONS

def tobytes(b1):
    b1_hex = format(int(b1), '02x')
    return binascii.unhexlify(b1_hex)
