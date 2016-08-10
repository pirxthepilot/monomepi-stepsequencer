import serial
import time
import binascii
import threading
import animation as a


# BEGIN 128-compat
LED_ON_CMD = '11'
LED_OFF_CMD = '10'
KEY_DN = '21'
KEY_UP = '20'
CLEAR_CMD = '12'
FILL_CMD = '13'
LED_ROW_CMD = '15'
LED_COL_CMD = '16'
DEFAULT_INTENSITY = '1980'
# END 128-compat


class Monome(object):

    def __init__(self, serial_port, baud=115200, led_state=[]):
        for i in range(128):    # 128 compat
            led_state.append('0')
        self.led_state = led_state
        self.serial_port = serial_port
        self.baud = baud
        self.keyin = {}
        self.exit_flag = False
        self.p_listener = PressListener(self)
        self.press = False

    def open_serial(self):
        self.ser = serial.Serial(self.serial_port, self.baud)
        self.ser.write(binascii.unhexlify(DEFAULT_INTENSITY))
        a.start_animation(self)
        self.p_listener.start()

    def close_serial(self):
        time.sleep(1)
        a.end_animation(self)
        self.call_exit()
        self.ser.close()

    def check_led_states(self):
        print
        for i in range(len(self.led_state)):
            if i % 8 == 0:
                print '\n' + str(self.led_state[i]),
            else:
                print self.led_state[i],

    def get_led(self, x, y):
        assert(isinstance(x, str))
        assert(isinstance(y, str))
        # state = self.led_state[int(str(y)+str(x), 8)]
        state = self.led_state[int(str(y)+str(x), 16)]  # 128 compat
        return state

    def set_led(self, state, x, y, light_feedback=True):
        s = ''
        if state == LED_ON_CMD:
            s = '1'
        if state == LED_OFF_CMD:
            s = '0'
        # self.led_state[int(str(y)+str(x), 8)] = s
        self.led_state[int(str(y)+str(x), 16)] = s  # 128 compat
        if light_feedback:
            cmd = state + '0'+str(x) + '0'+str(y)
            self.ser.write(binascii.unhexlify(cmd))
            # print 'Set command is ' + cmd

    def set_led_nostate(self, state, x, y):     # Only set the light but not actual state
        cmd = state + '0'+str(x) + '0'+str(y)
        self.ser.write(binascii.unhexlify(cmd))

    def set_via_buffer(self, led_buffer):
        c = ''
        cmd = ''
        self.led_state = list(led_buffer)
        for i in range(len(self.led_state)):
            xy = GridCoord(i)
            if self.led_state[i] == '1':
                cmd = LED_ON_CMD + '0'+str(xy.x) + '0'+str(xy.y)
            if self.led_state[i] == '0':
                cmd = LED_OFF_CMD + '0'+str(xy.x) + '0'+str(xy.y)
            self.ser.write(binascii.unhexlify(cmd))

    def set_all(self, state):
        if state == 0:
            self.ser.write(binascii.unhexlify(CLEAR_CMD))   # 128-compat
        if state == 1:
            self.ser.write(binascii.unhexlify(FILL_CMD))    # 128-compat

    def read_keys(self):
        out_string = binascii.hexlify(self.ser.read(3))
        # print "Read: " + out_string
        assert(isinstance(out_string, str))
        if len(out_string) == 6:
            self.keyin['c'] = out_string[0:2]
            self.keyin['x'] = out_string[3:4]
            self.keyin['y'] = out_string[5:6]
            # print '  c=' + self.keyin['c'] + ' x=' + self.keyin['x'] + ' y=' + self.keyin['y']
            return True
        else:
            return False

    def toggle(self):
        if self.keyin['c'] == KEY_DN:
            if self.get_led(self.keyin['x'], self.keyin['y']) == '0':
                self.set_led(LED_ON_CMD, self.keyin['x'], self.keyin['y'])
            elif self.get_led(self.keyin['x'], self.keyin['y']) == '1':
                self.set_led(LED_OFF_CMD, self.keyin['x'], self.keyin['y'])

    def trigger(self):
        if self.keyin['c'] == KEY_DN:
            self.set_led(LED_ON_CMD, self.keyin['x'], self.keyin['y'])
        elif self.keyin['c'] == KEY_UP:
            self.set_led(LED_OFF_CMD, self.keyin['x'], self.keyin['y'])

    def state_only(self):
        if self.keyin['c'] == KEY_DN:
            self.set_led(LED_ON_CMD, self.keyin['x'], self.keyin['y'], light_feedback=False)
        elif self.keyin['c'] == KEY_UP:
            self.set_led(LED_OFF_CMD, self.keyin['x'], self.keyin['y'], light_feedback=False)

    def reset_keyin(self):
        self.keyin['c'] = ''
        self.keyin['x'] = ''
        self.keyin['y'] = ''

    def set_row(self, hexrow, hexdata):
        # cmd = LED_ROW_CMD + hexrow + hexdata
        cmd = LED_ROW_CMD + '00' + '0'+hexrow + hexdata  # 128-compat
        self.ser.write(binascii.unhexlify(cmd))

    def set_col(self, hexcol, hexdata):
        # cmd = LED_COL_CMD + hexcol + hexdata
        cmd = LED_COL_CMD + '0'+hexcol + '00' + hexdata  # 128-compat
        self.ser.write(binascii.unhexlify(cmd))

    def is_off(self):
        if '1' in self.led_state:
            return False
        else:
            return True

    def call_exit(self):
        self.exit_flag = True


class PressListener(threading.Thread):

    def __init__(self, monome_instance):
        print 'Starting Press Listener.'
        threading.Thread.__init__(self)
        self.monome_instance = monome_instance

    def run(self):
        while not self.monome_instance.exit_flag:
            if self.monome_instance.read_keys():
                self.monome_instance.press = True
            time.sleep(0.01)
        print 'Press Listener thread exit.'


class GridCoord:
    def __init__(self, n):
        self.y = int(oct(n)[len(oct(n))-2])
        self.x = int(oct(n)[len(oct(n))-1])


def translate(c):
    out = ''
    if c == KEY_DN:
        out = LED_ON_CMD
    if c == KEY_UP:
        out = LED_OFF_CMD
    return out
