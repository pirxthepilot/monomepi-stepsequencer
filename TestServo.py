from servo2 import Servo
from servocontrol import ServoControl
from time import sleep

STEP_TIME = '10'    # in milliseconds
STEP_AMT = '1'
RIGHT_X = '5'
RIGHT_Y = '7'
LEFT_X = '2'
LEFT_Y = '7'
SWEEP_X = '4'
SWEEP_Y = '7'
EXIT_X = '7'
EXIT_Y = '7'


# INIT
#
a = Servo('/dev/ttyACM0')
a.open_servo()


# MAIN
#

servothreads = []
s4 = ServoControl(a, '4')
servothreads.append(s4)
s5 = ServoControl(a, '5')
servothreads.append(s5)

for t in servothreads:
    t.start()

while True:
    try:
#        s4.hit = True
#        sleep(0.5)
        s4.hit = True
        s5.hit = True
        sleep(0.5)
    except KeyboardInterrupt:
        for t in servothreads:
            t.exit_flag = True
            print "\nExit servo " + t.servo
        break


a.close()
print "Done."
