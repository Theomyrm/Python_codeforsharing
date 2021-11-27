"""                 TURTLE CODE COLLECTION                   """
#    """"""""""""""""""""""""""""""""""""""""""""""""""""""    #
"""                                                          """ 
"""
                   Turtle code collection:

              A personal collection of turtle
         code for all purposes. Feel free to take 
                  any code from here.
                                        T. Myrm
"""

  ## * - * - ## * - * - ## Libraries ## * - * - ## * - * ##

import turtle as t                 ##  Our guy  ## 
from time import sleep     ##  Works a lot. Everyone knows  ##
import math as m           ##  Need this for juicy stuff    ##
import random as rnd       ##  Everything is chaos          ##

  ## * - * - ## * - * - ## * - * - ## * - * - ## * - * - ##


  ################ Creating turtle setups ##################
  ## Windows: lets make windows with pride and joy!, it's ##
  ## better to define our workspace from the beginning.   ##
  ## Also, comment all the code you don't want to try/use.##
  ##########################################################  
  
def makeWindow():
    window = t.Screen()    ## The most basic configuration ##
    #window.bgcolor('pink') ## Show the world your fashion  ##
    window.title('Crazy Johnys evil threath') ## Title, yes ##
    #window.exitonclick()   ## Click it ##


  ################ Creating turtle objects #################
  ## Its a good idea to create turtle objects as classes  ##
  ## If you want to make things with more interactivity   ##
  ##########################################################

  ######################    QUOTE    ####################### 
  # This code was created by BashBedlam. Link for the code:#
  # URL:   https://python-forum.io/thread-34638.html       #
  ##########################################################

                                #################################
class Turtle_object(t.Turtle):  ### THIS IS YOUR TURTLE DUMMY ###   
                                #################################
    def __init__(self):         ### Put whatever arguments    ###
        t.Turtle.__init__(self) ### you want as Turtle        ###
        self.penup()            ### Attributes.               ### 
        self.hideturtle()       ### This example is a Turtle  ###  
        self.speed(0)           ### Made for doing walls      ###
        self.pensize(5)         ###                           ###
                                ###                           ###
    def draw_line(self):        ### Write new functions to    ###
        self.penup()            ### Make your Turtle do stuff ###   
        self.goto(-200, -200)   ### This one makes a line     ###
        self.pendown()          ### like this one:            ### 
        self.goto(-200, 200)    ###           y = 200         ###
                                ###             ^             ###
                                ### x ---------|||---------   ###
                                ###             |             ###
                                ###             |             ###
                                ###             |             ###
                                ###           y = -200        ###
                                #################################


""" /-\  /-\  /-\  /-\    Test zone     /-\  /-\  /-\  /-\ """
  
    ## Just put in there the functions you want to test ##
    ## At your own risk.                                ##
  
makeWindow()


         ###       ###     Test Box     ###       ###

line = Turtle_object()
line.draw_line()










