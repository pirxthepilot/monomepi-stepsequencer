from time import sleep
from servo2 import Servo
from servocontrol import ServoControl
from monomepi128 import Monome, Button, ButtonHandler

BPM = 120
EXIT_X = 'f'
EXIT_Y = '7'


# Methods
#

def check_if_exit(monome):
    if monome.get_led(EXIT_X, EXIT_Y) == '1':
        monome.call_exit()
        return monome.exit_flag


# INIT monome
#
m = Monome('/dev/ttyUSB0')

# Make all buttons toggle buttons
buttons = []
for xbutt in range(16):
    for ybutt in range(8):
        buttons.append(Button(m, int(xbutt), int(ybutt), 'toggle'))

m.open_serial()
button_thread = ButtonHandler(m, buttons)
button_thread.start()


# INIT servos
a = Servo('/dev/ttyACM0')
a.open_servo()

servos = []
servos.append(ServoControl(a, '0'))
servos.append(ServoControl(a, '1'))
servos.append(ServoControl(a, '2'))
servos.append(ServoControl(a, '3'))
servos.append(ServoControl(a, '4'))
servos.append(ServoControl(a, '5'))
servos.append(ServoControl(a, '6'))
servos.append(ServoControl(a, '7'))

for st in servos:
    st.start()
    sleep(0.05)
    a.reset(st.servo)


# MAIN
#

col = 0
prevcol = 0
enabled_rows = []

while not check_if_exit(m):

    # Light up column and reset previous column LEDs
    m.set_col(str(format(int(col), '01x')), 'FF')
    for row in enabled_rows:
        m.set_led_nostate('11', str(format(prevcol, '01x')), str(row))

    # Fire appropriate servos and store current
    # column's LED states
    enabled_rows = []
    for row in range(8):
        if m.get_led(str(format(col, '01x')), str(row)) == '1':
            servos[row].hit = True
            enabled_rows.append(row)

    # Delay (based on BPM)
    sleep(float(60) / float(BPM))

    # Turn off column LEDs and move to next
    m.set_col(str(format(int(col), '01x')), '00')
    prevcol = col
    col = (col + 1) % 16


# EXIT
#
sleep(1)
m.close_serial()
for st in servos:
    st.exit_flag = True
a.close()

print "All done."
