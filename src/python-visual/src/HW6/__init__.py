from __future__ import division
from visual import *
scene.background = color.white
scene.width = 800
scene.height = 800
import math, time

def grid(max=10, rad=0.03):
    gray = (0.8, 0.8, 0.8)
    for x in range(-max, max + 1, 1):  # # parallel to z axis,  vary x
        cylinder(pos=(x, 0, -max), axis=(0, 0, 2 * max), radius=rad, color=gray, opacity=0.2)
    for z in range(-max, max + 1, 1):  # # parallel to x axis, vary z
        cylinder(pos=(-max, 0, z), axis=(2 * max, 0, 0), radius=rad, color=gray, opacity=0.2)
    for y in range(-max, max + 1, 1):  # # parallel to z axis, vary y
        cylinder(pos=(0, y, -max), axis=(0, 0, 2 * max), radius=rad, color=gray, opacity=0.2)
    for z in range(-max, max + 1, 1):  # # parallel to y axis, vary z
        cylinder(pos=(0, -max, z), axis=(0, 2 * max, 0), radius=rad, color=gray, opacity=0.2)

def axes(max=10, rad=0.1):
    xaxis = cylinder(color=(1, 0, 0), pos=(-max, 0, 0), axis=(2 * max, 0, 0), radius=rad)
    xlbl = label(pos=(11, 0, 0), text="X", color=color.red, opacity=0, height=30)
    yaxis = cylinder(color=color.green, pos=(0, -max, 0), axis=(0, 2 * max, 0), radius=rad)
    ylbl = label(pos=(0, 11, 0), text="Y", color=color.green, opacity=0, height=30)
    zaxis = cylinder(color=color.blue, pos=(0, 0, -max), axis=(0, 0, 2 * max), radius=rad)
    xlbl = label(pos=(0, 0, 11), text="Z", color=color.blue, opacity=0, height=30)


grid()
axes()

'''VARIABLES'''
center_of_room = (5, 0, 5)
origin = (1, 0, 1)
deltat = 0.001
vpuck = vector(1, 0, 1)  # distance puck traveled per second
t = 0.0
x = 0

'''OBJECTS'''
floor_ice = box(pos=center_of_room, length=10, height=0, width=10, color=color.white)
puck = cylinder(pos=origin, axis=(0, 1, 0), radius=1, color=color.black)


while t <= 8.0:
    t = t + deltat
    puck.pos = puck.pos + (vpuck * deltat)
    print t
    rate(1000)
x = x + 1



