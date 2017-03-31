#!/usr/bin/env python
'''
Flashes on and off LED USR0. 

Takes two arguments 'count' and 'period'.
'count' is an integer representing number of times LED cycles on and off.
'period' is a float representing the delay between on->off and off->on cycle.

IMPORTANT: Requires root privileges

Author: Carlos L. Torres 2017
'''
from __future__ import print_function


import sys
import time

def main():
    if len(sys.argv) != 3:
       print('Usage: blink_led <count> <period>')
       sys.exit(-1)

    COUNT = int(sys.argv[1])
    PERIOD = float(sys.argv[2])
    USR0_LED = '/sys/class/leds/beaglebone:green:usr0/brightness'

    i = COUNT
    while i > 0:
        with open(USR0_LED, 'w') as led0:
            led0.write('1')
        time.sleep(PERIOD)
        with open(USR0_LED, 'w') as led0:
            led0.write('0')
        time.sleep(PERIOD)
        i -= 1



if __name__ == '__main__':
    main()

