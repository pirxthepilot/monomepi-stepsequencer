from servo_step import Servo
from servocontrol import ServoControl
from time import sleep


# INIT
#
a = Servo('/dev/ttyACM0')
a.open_servo()


# MAIN
#

servothreads = []
c1 = ServoControl(a, '0')
d1 = ServoControl(a, '1')
e1 = ServoControl(a, '2')
f1 = ServoControl(a, '3')
g1 = ServoControl(a, '4')
a1 = ServoControl(a, '5')
b1 = ServoControl(a, '6')
c2 = ServoControl(a, '7')

servothreads.append(c1)
#servothreads.append(d1)
#servothreads.append(e1)
#servothreads.append(f1)
#servothreads.append(g1)
#servothreads.append(a1)
#servothreads.append(b1)
#servothreads.append(c2)

for st in servothreads:
    st.start()

while True:
    try:
        for st in servothreads:
            st.hit = True
        sleep(1)
    except KeyboardInterrupt:
        for st in servothreads:
            st.exit_flag = True
            print "\nExit servo " + st.servo
        break

a.close()
print "Done."
