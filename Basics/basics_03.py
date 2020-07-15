# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 13:56:33 2020

@author: jfarm
"""
from random import randint
from turtle import Turtle, Screen

def main():
    t = Turtle()
    s = Screen()
    
    size = randint(10, 50)
    
    
    
    # for i in range(4):    
    #     t.forward(size)
    #     t.right(90)

    s.mainloop()

if __name__ == '__main__':
    main()