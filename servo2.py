from arduinopi import Arduino
import binascii


# CMD_PAD = 0.01      # Padding for servo command delays
INIT_POS = '80'     # Servo's initial position (defined in sketch as initpos)
MIN_POS = '5'       # Servo's safe minimum position
MAX_POS = '160'     # Servo's accepted maximum angle


class Servo(Arduino):

    def __init__(self, serial_port):
        super(Servo, self).__init__(serial_port)
        self.currentpos = INIT_POS
        self.minpos = MIN_POS
        self.maxpos = MAX_POS

    def open_servo(self):
        self.open()

    def move(self, motions):
        for motion in motions:
            servo = motion[0]
            pos = motion[1]
            if pos == 'pause':
                pos = self.currentpos
            elif int(pos) > int(self.maxpos):
                pos = self.maxpos
            elif int(pos) < 0:
                pos = self.minpos
            #print "Move servo " + servo + " to position [" + pos + "]"
            self.write(tobytes(servo, pos))
            self.currentpos = pos

    def reset(self, servo):
        motion = [(servo, INIT_POS)]
        self.move(motion)


# FUNCTIONS

def tobytes(b1, b2):
    b1_hex = format(int(b1), '02x')             # SERVO POSITION = 1 byte
    b2_hex = format(int(b2), '02x')             # SERVO DELAY (ms) = 2 bytes
    # print "Delay in hex: " + b2_hex
    return binascii.unhexlify(b1_hex + b2_hex)  # Total = 3 bytes sent!
