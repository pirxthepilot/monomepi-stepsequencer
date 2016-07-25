import threading


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
                self.servo_instance.move(self.servo)
                self.hit = False
        # print "Exit servocontrol " + self.servo
