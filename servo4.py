from arduinopi import Arduino
from time import sleep
import binascii
import threading


# CMD_PAD = 0.01      # Padding for servo command delays
INIT_POS = '80'     # Servo's initial position (defined in sketch as initpos)
MIN_POS = '5'       # Servo's safe minimum position
MAX_POS = '160'     # Servo's accepted maximum angle


class Servo(Arduino):

    def __init__(self, serial_port, servo):
        super(Servo, self).__init__(serial_port)
        self.servo = servo
        self.currentpos = INIT_POS
        self.minpos = MIN_POS
        self.maxpos = MAX_POS

    def open_servo(self):
        self.open()
        # intro = [(str(int(INIT_POS)+30), '100'), ('4', INIT_POS, '300')]
        # for i in range(0, 3):
        #     self.move(intro)

    def _move(self, motions):
        for motion in motions:
            pos = motion[0]
            dly = motion[1]
            if pos == 'pause':
                pos = self.currentpos
            elif int(pos) > int(self.maxpos):
                pos = self.maxpos
            elif int(pos) < 0:
                pos = self.minpos
            print "Move to position [" + pos + "] in [" + dly + "ms]"
            self.write(tobytes(self.servo, pos))
            self.currentpos = pos
            sleep(computedelay(dly))

    def move(self, motions):
        threading.Thread(target=self._move, args=(motions,)).start()

    def reset(self):
        motion = [(INIT_POS, '800')]
        self.move(motion)


# FUNCTIONS

def tobytes(b1, b2):
    b1_hex = format(int(b1), '02x')             # SERVO POSITION = 1 byte
    b2_hex = format(int(b2), '02x')             # SERVO DELAY (ms) = 2 bytes
    # print "Delay in hex: " + b2_hex
    return binascii.unhexlify(b1_hex + b2_hex)  # Total = 3 bytes sent!


def computedelay(dly):
    insecs = float(float(dly)/1000)
    # return insecs + CMD_PAD
    return insecs
