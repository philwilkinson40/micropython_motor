#Simple script for stepper motor 

import machine 
import time 

d1 = machine.Pin(5, machine.Pin.OUT) 
d2 = machine.Pin(4, machine.Pin.OUT) 
d3 = machine.Pin(0, machine.Pin.OUT) 
d4 = machine.Pin(2, machine.Pin.OUT) 

def move(direction='counterclockwise'):
    pins=[d1,d2,d3,d4]
    if direction=='clockwise':
        pins.reverse()

    for steps in range(250):
        for i in pins:
            i.value(1); time.sleep(0.005); i.value(0)
        steps+=1

move()
move('clockwise')
