from arduinopi import Arduino
from time import sleep
import binascii


def tobytes(b1, b2):
    b1_hex = format(int(b1), '02x')     # 1 byte
    b2_hex = format(int(b2), '02x')     # 1 byte
    print "Delay in hex: " + b2_hex
    return binascii.unhexlify(b1_hex+b2_hex)



a = Arduino('COM5')
a.open()

pos = '60'
dly = '100'
print "Sending data.."
a.write(tobytes(pos, dly))

sleep(1)

pos = '100'
dly = '250'
print "Sending data.."
a.write(tobytes(pos, dly))

print "Done."
sleep(1)
a.close()
