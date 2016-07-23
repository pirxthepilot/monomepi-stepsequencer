from threading import Thread
from servo4 import Servo
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
a = Servo('/dev/ttyACM0', '4')
b = Servo('/dev/ttyACM0', '5')
a.open_servo()
b.open_servo()


# MAIN
#

flick = [('40', '2000'), ('120', '2000')]
m1 = [('10', '800'), ('120', '800')]
m2 = [('10', '800'), ('120', '800')]
a.move(flick)
b.move(flick)
sleep(0.2)
a.move(flick)
b.move(flick)
sleep(1)
a.reset()
#sleep(0.2)
b.reset()
sleep(0.2)
a.close()
b.close()
print "Done."
