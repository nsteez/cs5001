"""
Netti Welsh
CS5001 - Fall202
Lab 9 - Turtle
"""
import turtle

Screen = turtle.Screen()
turt = turtle.Turtle() # Create a variable of data type Turtle, with label turt

turt.pensize(2)


circ = ['green','blue','orange','red', 'yellow']


for i in range(5):
    turt.speed(3)
    turt.pencolor(circ[i])
    turt.right(288)
    turt.forward(150)
    turt.left(144)


turtle.done()