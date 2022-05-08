#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.media.ev3dev import Font
import time

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
ev3.screen.clear()
# Write your program here.
big_font = Font(size=200, bold=True)
# a = minutes
# b = seconds
timer = int(25)
second_timer = int(timer * 60)
minutes = int(second_timer/60) - 1
seconds = 60
for x in range(second_timer):
    time.sleep(1)
    seconds = int(seconds)
    seconds -= 1
    if seconds < 0:
        minutes -= 1
        seconds = 59
    if seconds < 10:
        seconds = '0' + str(seconds)
    str_minutes = str(minutes)
    str_seconds = str(seconds)
    final_time = str(str_minutes + ':' + str_seconds)
    ev3.screen.clear()
    ev3.screen.set_font(big_font)
    ev3.screen.draw_text(50, 50, final_time)
    if final_time = '0:00':
        ev3.speaker.play_file(READY)