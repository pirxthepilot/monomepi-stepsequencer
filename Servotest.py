from math import floor
from servo2 import Servo
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



# motions = [('70','100'), ('50','250'), ('80','200'), ('40','250'), ('90','500'), ('30','300'), ('100','1000'), ('20','500'), ('110','1000'), ('10','1200')]
sleep(2)
motions = [('10','1000'), ('60','1000'), ('120','1000')]
a.move(motions)
sleep(2)
a.reset()
a.close()
print "Done."
