from turtle import *
import turtle

speed(0)
setup(800, 500)

penup()
goto(-400, 250)
pendown()

# red Rectangle
color("red")
begin_fill()
forward(800)
right(90)
forward(167)
right(90)
forward(800)
end_fill()

left(90)
forward(167)

# black Rectangle
color("black")
begin_fill()
forward(167)
left(90)
forward(800)
left(90)
forward(167)
end_fill()

win=turtle.Screen( )
win.setup(width = 800, height = 600)
win.bgpic('output-onlinepngtools (1).png')
turtle.done( )
# Spokes
penup()
goto(0, 0)
pendown()
pensize(2)
for i in range(24):
    forward(60)
    backward(60)
    left(15)
    
    
hideturtle()
