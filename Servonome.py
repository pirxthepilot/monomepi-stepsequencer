from arduinopi import Arduino
from time import sleep
import binascii


def move(motions):
    for motion in motions:
        pos = motion[0]
        dly = motion[1]
        if pos == 'pause': pos = currentpos
        print "Move to position [" + pos + "] in [" + dly + "ms]"
        a.write(tobytes(pos, dly))
        currentpos = pos
        sleep(computedelay(dly))

def tobytes(b1, b2):
    b1_hex = format(int(b1), '02x')     # 1 byte
    b2_hex = format(int(b2), '02x')     # 1 byte
    #print "Delay in hex: " + b2_hex
    return binascii.unhexlify(b1_hex+b2_hex)

def computedelay(dly):
    insecs = float(int(dly)/1000)
    pad = 0.005
    return insecs + pad


a = Arduino('COM5')
a.open()

currentpos = '90'
motions = [('110','100'), ('90','250'), ('30','200'), ('pause', '250'), ('90','250')]
move(motions)


print "Done."
sleep(1)
a.close()
