import threading
from time import sleep


# Issues the commands to the Servo object
# One instance per servo
class ServoControl(threading.Thread):

    def __init__(self, servo_instance, servo):
        super(ServoControl, self).__init__()
        self.servo_instance = servo_instance
        self.servo = servo
        self.hit = False
        self.exit_flag = False

    def run(self):
        while not self.exit_flag:
            if self.hit:
                self.hit_motion()
                self.hit = False
        #print "Exit servocontrol " + self.servo

    def hit_motion(self):
        motions = [(self.servo, '120')]
        self.servo_instance.move(motions)
        sleep(.08)
        # motions = [(self.servo, '80')]
        # self.servo_instance.move(motions)
        self.servo_instance.reset(self.servo)
