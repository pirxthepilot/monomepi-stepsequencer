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

s3[0] = '1'
s3[1] = '0'
s3[2] = '0'
s3[3] = '1'
s3[4] = '0'
s3[5] = '1'
s3[6] = '0'
s3[7] = '0'

new = ''.join(list(reversed(s3)))

while True:
    try:
        #a.move(s1)
        #print s1
        #sleep(1)
        a.move(int(new, 2))
        print new
        sleep(1)
    except KeyboardInterrupt:
        print "\nExit"
        break

a.close()
print "Done."
