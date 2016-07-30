from servo_step import Servo
from time import sleep


# INIT
#
a = Servo('/dev/ttyACM0')
a.open_servo()


# MAIN
#

s1 = '00000101'
s2 = '00000110'

s3 = ['0' for i in range(8)]

s3[0] = '00000101'
s3[1] = '00001010'
s3[2] = '00010100'
s3[3] = '0'
s3[4] = '1'
s3[5] = '0'
s3[6] = '0'
s3[7] = '1'


while True:
    try:
        for i in range(8):
        #a.move(s1)
        #print s1
        #sleep(1)
            new = ''.join(list(reversed(s3[i])))
            a.move(format(int(new, 2), '02x'))
        print new
        sleep(1)
    except KeyboardInterrupt:
        print "\nExit"
        break

a.close()
print "Done."
