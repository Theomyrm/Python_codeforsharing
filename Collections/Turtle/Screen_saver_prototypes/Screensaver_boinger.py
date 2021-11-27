#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import turtle as t
import random as rnd
from time import sleep
import math as m

"""
Screen saverrrrr

"""

t.setworldcoordinates(-500, -500, 500, 500)
window = t.Screen()    ## The most basic configuration ##
#window.bgcolor('pink') ## Show the world your fashion  ##
window.title('Crazy Johnys evil threath') ## Title, yes ##
   ## Click it ##




class Container(t.Turtle):
  
    def __init__(self, cont_color, pensize_cont):
        t.Turtle.__init__(self)
        self.penup() 
        self.hideturtle()
        self.speed(0)
        self.cont_color = cont_color
        self.color(cont_color)
        #self.pensize_cont = pensize_cont  ### Si no funciona probar
        self.pensize(pensize_cont)
         
  
    def draw_shape(self, size, shape_cont):
        self.size = size
        self.penup()
        self.goto(0, 0)
        self.pendown()
        self.shape_cont = shape_cont ## Number of sides; figure
        
        for i in range(shape_cont):    
            self.fd(size)
            self.lt(360/shape_cont)

#################################################

def isCollision(t1, t2):
        if abs (t1.xcor () - t2.xcor ()) < 20 :
            a = t1.ycor ()
            b = t2.ycor ()
            if a < b and a > b - 400 :
                return True
        else:
            return False

##################################################

class Boinger(t.Turtle):
    
    def __init__(self, boinger_speed, boinger_shape):
        t.Turtle.__init__(self)
        self.speed(boinger_speed)
        self.shape(boinger_shape)
        self.penup()
        self.setpos((rnd.randint(20, 150)),(rnd.randint(50, 380)))
    
    def boing(self, container, angle1, angle2):
       while True:
           self.fd(10)
           if isCollision(self, container):
               self.lt(rnd.randint(angle1, angle2))
        
            
##############################################################################


boing = Boinger(2, 'triangle')
sq = Container('black', 3)


sq.draw_shape(750, 4)
sleep(2)
boing.boing(sq, 45, 65)


   

            
            
        
        
    





