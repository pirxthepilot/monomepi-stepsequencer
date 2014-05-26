import monomepi128 as m
import time
import random


def blink_all(inst, endstate = 0):
    for i in range(9):
        inst.set_all(0)
        time.sleep(0.04)
        inst.set_all(1)
        time.sleep(0.04)
    inst.set_all(endstate)


def start_animation(inst):
    blink_all(inst, 1)
    time.sleep(0.4)
    randset = [ random.randint(0, 7) ]
    while len(randset) < 8:
        n = random.randint(0,7)
        if n not in randset:
            randset.append(n)
    for i in range(len(randset)):
        inst.set_col(str(randset[i]), '00')
        time.sleep(0.1)
    inst.set_all(0)


def end_animation(inst):
    for i in range(7, -1, -1):
        inst.set_row(str(i), 'FF')
        time.sleep(0.1)
    time.sleep(0.2)
    blink_all(inst)
