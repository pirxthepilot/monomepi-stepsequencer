import monomepi128 as m
import time
from collections import namedtuple

ANIMATION_SPEED = 0.12
WRAP = False


class Organism:

    def __init__(self, pos, led_state):    # Decimal int coordinates
        octpos = m.GridCoord(pos)          # Convert to octal for parsing
        mod = 8
        # NOTE: All variables are ultimately decimal ints
        #
        self.led_state = led_state
        self.now = pos
        nbr = { v: True for v in ('n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw') }
        if not WRAP:
            if octpos.y == 0:                   nbr['n'] = False
            if octpos.y == 0 or octpos.x == 7:  nbr['ne'] = False
            if octpos.x == 7:                   nbr['e'] = False
            if octpos.y == 7 or octpos.x == 7:  nbr['se'] = False
            if octpos.y == 7:                   nbr['s'] = False
            if octpos.y == 7 or octpos.x == 0:  nbr['sw'] = False
            if octpos.x == 0:                   nbr['w'] = False
            if octpos.y == 0 or octpos.x == 0:  nbr['nw'] = False

        if nbr['n']:  nbr['n'] = int(str((octpos.y-1)%mod) + str(octpos.x), 8) 
        if nbr['ne']: nbr['ne'] = int(str((octpos.y-1)%mod) + str((octpos.x+1)%mod), 8)
        if nbr['e']:  nbr['e'] = int(str(octpos.y) + str((octpos.x+1)%mod), 8)
        if nbr['se']: nbr['se'] = int(str((octpos.y+1)%mod) + str((octpos.x+1)%mod), 8)
        if nbr['s']:  nbr['s'] = int(str((octpos.y+1)%mod) + str(octpos.x), 8)
        if nbr['sw']: nbr['sw'] = int(str((octpos.y+1)%mod) + str((octpos.x-1)%mod), 8)
        if nbr['w']:  nbr['w'] = int(str(octpos.y) + str((octpos.x-1)%mod), 8)
        if nbr['nw']: nbr['nw'] = int(str((octpos.y-1)%mod) + str((octpos.x-1)%mod), 8)
        self.nbr = nbr

    def get_fate(self):
        neighbors = 0
        fate = 'unknown'
        for i,j in self.nbr.iteritems():
            if j:
                if self.led_state[int(j)] == '1':
                    neighbors += 1
        # Game logic here!
        if self.led_state[self.now] == '0':
            if neighbors == 3:
                fate = 'alive'
            else:
                fate = 'dead'
        elif neighbors == 2 or neighbors == 3:
            fate = 'alive'
        else:
            fate = 'dead'
        return fate
        

def gameOfLife(instance):
    
    led_buffer = [0 for i in range(64)]
    exit_invoked = False
    
    while not exit_invoked:
        
        print 'Begin!'
        while True:
            if instance.read_keys():
                instance.toggle()
            # Start button!
            if instance.keyin['x'] == '7' and instance.keyin['y'] == '7':
                print 'Running...'
                break

        instance.ser.timeout = ANIMATION_SPEED/2
        hold_time = 1 # Secs to hold button (to stop)
        hold = 0

        while not instance.is_off():
            time.sleep(ANIMATION_SPEED/2)
            for i in range(len(led_buffer)):
                life = Organism(i, instance.led_state)
                state = life.get_fate()
                if state == 'alive':
                    led_buffer[i] = '1'
                if state == 'dead':
                    led_buffer[i] = '0'
            instance.set_via_buffer(led_buffer)
            # Runtime input allowed :)
            if instance.read_keys():
                instance.toggle()
            # Stop button is same as start button - hold to stop
            if instance.keyin['x'] == '7' and instance.keyin['y'] == '7':
                if instance.keyin['c'] == m.KEY_DN:
                    hold += 1
                elif instance.keyin['c'] == m.KEY_UP:
                    hold = 0
            elif hold > 0: hold += 1
            if hold*ANIMATION_SPEED > hold_time:
                print 'Exit invoked!'
                exit_invoked = True
                break
            #print hold
            instance.reset_keyin()
        


joon = m.Monome('COM6', 115200)
joon.open_serial()

gameOfLife(joon)

#joon.call_exit()
joon.close_serial()
