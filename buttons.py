import serial
import time
import binascii
import threading
import animation as a


TICK = 0.01


class Button(object):

    def __init__(self, monome_instance, x, y, buttontype, speed=0):
        self.monome_instance = monome_instance
        #self.x = str(x)
        #self.y = str(y)
        self.x = str(format(x, '01x'))  # 128 compat
        self.y = str(format(y, '01x'))  # 128 compat
        assert(buttontype == 'none' or
               buttontype == 'toggle' or
               buttontype == 'trigger' or
               buttontype == 'blink'), 'Invalid buttontype!'
        self.buttontype = buttontype
        self.speed = int((speed/TICK)*2)    # converted to ticks
        self.ticker = 0                     # for blinks

    def is_on(self):
        if self.monome.get_led(self.x, self.y) == '1':
            return True
        else:
            return False


class ButtonHandler(threading.Thread):

    def __init__(self, monome_instance, buttons):
        threading.Thread.__init__(self)
        self.monome_instance = monome_instance
        self.buttons = buttons

    def run(self):
        while not self.monome_instance.exit_flag:
            # Input response
            if self.monome_instance.press:
                for butt in self.buttons:
                    if self.monome_instance.keyin['x'] == butt.x and self.monome_instance.keyin['y'] == butt.y:
                        if butt.buttontype == 'trigger':
                            self.monome_instance.trigger()
                        elif butt.buttontype == 'toggle' or butt.buttontype == 'blink':
                            self.monome_instance.toggle()
                self.monome_instance.press = False
            time.sleep(0.01)
            # Blinker
##            for butt in self.buttons:
##                if butt.buttontype == 'blink' and self.monome_instance.get_led(butt.x, butt.y) == '1':
##                    butt.ticker += 1
##                    butt.ticker = butt.ticker % butt.speed
##                    if butt.ticker == 0:
##                        self.monome_instance.set_led_nostate(LED_ON_CMD, butt.x, butt.y)
##                    elif butt.ticker == butt.speed/2:
##                        self.monome_instance.set_led_nostate(LED_OFF_CMD, butt.x, butt.y)
##            time.sleep(TICK)
        print 'Button Handler thread exit.'
