#!/usr/bin/env python

import time
import turtle
import math
c = 9.375

screen = turtle.Screen()
screen.colormode(255)
t = turtle.Turtle()
t.shape("blank")
t.penup()
t.sety(-18)
t.pendown()

h = 22.5
for i in range(0, 360, 45):
    t.setheading(h + i)
    t.forward(14)

n = turtle.Turtle()
n.shape("circle")
n.penup()
n.speed(0)

def updateTurtleAngle(angle):
    n.setx(10 * math.sqrt(2) * math.cos(math.radians(angle)))
    n.sety(10 * math.sqrt(2) * math.sin(math.radians(angle)))

def updateTurtle():
    n.setx(wm.state['nunchuk']['stick'][0]/c)
    n.sety(wm.state['nunchuk']['stick'][1]/c)

def main():
    a = 45
    for i in range(45, 361, 45):
        updateTurtleAngle(i)
        time.sleep(0.5)
    n.setx(0)
    n.sety(0)
                         
if __name__ == '__main__':
    main()
