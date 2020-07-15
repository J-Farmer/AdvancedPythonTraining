# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 13:57:37 2020

@author: jfarm
"""
from turtle import Turtle, Screen
from random import randint

def main():
    t = Turtle()
    s = Screen()
    
    s.bgcolor("black")
    t.color("cyan")
    t.speed(0)
    t.penup()
    
    colors = ["hot pink", "orange", "cyan"]
    
    for dot in range(2000):
        x = randint(-500, 500)
        y = randint(-500, 500)
        
        t.goto(x,y)
        size = randint(10,75)
        if -500<=x<=-250:
            t.dot(size, colors[0])
        elif -250<=x<=250:
            t.dot(size, colors[1])
        else:
            t.dot(size, colors[2])
    
    s.mainloop()

if __name__ == '__main__':
    main()

