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
c1 = ServoControl(a, '4')
d1 = ServoControl(a, '5')
e1 = ServoControl(a, '6')
f1 = ServoControl(a, '7')
g1 = ServoControl(a, '8')
a1 = ServoControl(a, '9')
#b1 = ServoControl(a, '10')
#c2 = ServoControl(a, '11')
servothreads.append(c1)
servothreads.append(d1)
servothreads.append(e1)
servothreads.append(f1)
servothreads.append(g1)
servothreads.append(a1)
#servothreads.append(b1)
#servothreads.append(c2)

for st in servothreads:
    st.start()

while True:
    try:
        for st in servothreads:
            st.hit = True
        sleep(0.5)
    except KeyboardInterrupt:
        for st in servothreads:
            st.exit_flag = True
            print "\nExit servo " + st.servo
        break


a.close()
print "Done."
