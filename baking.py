#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import math
import time

def cir2aud(coord):
    """Convert from -1..-1 to 0..255 byte (character)."""
    return chr(int((coord+1.0)/2 * 255))

def emit(x, y):
    sys.stdout.write(cir2aud(y))
    sys.stdout.write(cir2aud(x))

def arm(x, y, steps, length=1.0):
    for i in range(steps, -1, -1) + range(0, steps+1, 1):
        emit(x * i / steps * length, y * i / steps * length)

def cyferblat():
    year, month, day, hours, minutes, seconds, weekday, yearday, isdst = time.localtime()
    arm1 = (hours % 12) + int(minutes/12)
    arm2 = minutes
    arm3 = seconds
    angle = 0.0
    steps = 60
    increment = 2.0 * math.pi / steps
    for step in xrange(steps):
        x = math.cos(angle)
        y = math.sin(angle)
        angle += increment
        if step % 5 == 0:
            dwell = 40
        else:
            dwell = 8
        for d in xrange(dwell/2):
            yield x, y
        if step == arm1:
            arm(x, y, 50, 0.5)
        if step == arm2:
            arm(x, y, 30, 0.7)
        if step == arm3:
            arm(x, y, 20, 0.9)
        for d in xrange(dwell/2):
            yield x, y

if sys.stdout.isatty():
    print >>sys.stderr, "I cowardly refuse to clobber thy teletype!"
    print >>sys.stderr, "Usage: ./baking.py | ./bread"
    print >>sys.stderr, "Also, is thy oscilloscope hooked up accordingly?"
    sys.exit(1)

while True:
    for x, y in cyferblat():
        emit(x, y)
