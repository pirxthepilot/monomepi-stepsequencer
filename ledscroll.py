from monomepi128 import Monome
from ledfont import ledmap
from time import sleep

EXIT_X = '7'
EXIT_Y = '7'
FREEZE_X = '0'
FREEZE_Y = '7'
LSCROLL_X = '1'
LSCROLL_Y = '7'
RSCROLL_X = '2'
RSCROLL_Y = '7'
MANUAL_SCROLL_SPEED = 0.04
ROW_SCROLL = False


class LedScroller(Monome):

    def __init__(self, serial_port):
        super(LedScroller, self).__init__(serial_port)
        self.messages = []
        self.freeze = False

    def push_msg(self, msg):
        self.messages.append(msg.encode('ascii', 'ignore'))
        #print self.messages

    def flush_all_msgs(self):
        del self.messages[:]

    def encode_msg(self, msg):
        col = [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 ]
        for t in msg:
            if self.is_ascii(t):
                col.extend(ledmap(ord(t)))
                if t != ' ':
                    col.append(0x00)    # add space between chars
        return col

    def is_ascii(self, char):
        if ord(char) >= 32 and ord(char) <= 127:
            return True
        else:
            return False
    
    def start_scroll(self, speed=0.1):
        disp = self.encode_msg(list(self.messages[0]))
        buffer_matrix = []
        scroll = 0
        while scroll < len(disp) + 8:
            if not self.check_if_freeze() or self.scroll_left() or self.scroll_right():
                # Set frame here
                for i in range(8):
                    if i+scroll >= len(disp):
                        setbit = 0x00
                    else:
                        setbit = disp[i+scroll]
                    bitvalue = self.preserve_control_row(setbit, i)
                    if ROW_SCROLL:
                        self.set_col(str(i), str(bitvalue))
                    else:
                        buffer_matrix.extend(bitlify(bitvalue))
                if not ROW_SCROLL:
                    buffer_matrix = matrix_rotate(buffer_matrix)
                    self.set_via_buffer(buffer_matrix)
                    buffer_matrix = []
                if self.scroll_left():
                    if scroll > 0:
                        sleep(MANUAL_SCROLL_SPEED)
                        scroll -= 1
                elif self.scroll_right():
                    sleep(MANUAL_SCROLL_SPEED)
                    scroll += 1
                else:
                    sleep(speed)
                    scroll += 1
            if self.check_if_exit():
                break

    def preserve_control_row(self, setbit, i):
        binrep = format(setbit, "08b")
        data = binrep[-7:]
        control = self.get_led(str(i), '7')
        return  format(int(control+data, 2), "02x")

    def check_if_exit(self):
        if self.get_led(EXIT_X, EXIT_Y) == '1':
            self.call_exit()
        return self.exit_flag

    def check_if_freeze(self):
        if not self.freeze:
            if self.get_led(FREEZE_X, FREEZE_Y) == '1':
                self.freeze = True
        elif self.freeze:
            if self.get_led(FREEZE_X, FREEZE_Y) == '0':
                self.freeze = False
        return self.freeze

    def scroll_left(self):
        if self.get_led(LSCROLL_X, LSCROLL_Y) == '1':
            return True
        else:
            return False

    def scroll_right(self):
        if self.get_led(RSCROLL_X, RSCROLL_Y) == '1':
            return True
        else:
            return False
            


def bitlify(bitvalue):
    out = []
    binned = str(format(int(bitvalue, 16), "08b"))
    for i in binned:
        out.extend(i)
    return out

def matrix_rotate(matrix):
    matrix2d = []
    for x in range(8): matrix2d.append([])

    for i in range(len(matrix)):
        matrix2d[(63-i)%8].append(str(matrix[63-i]))
    matrix = []
    matrix2d = zip(*matrix2d[::-1])
    matrix2d = zip(*matrix2d[::-1])
    for j in matrix2d:
        matrix.extend(j)
    return matrix



if __name__=="__main__":
    Scroller = LedScroller('COM6')
    Scroller.open_serial()
    while True:
        text = raw_input("Enter text: ")
        if text == 'exit':
            print 'Exit!'
            break
        Scroller.push_msg(text)
        Scroller.start_scroll()
        Scroller.flush_all_msgs()
    Scroller.call_exit()
    Scroller.close_serial()
    
