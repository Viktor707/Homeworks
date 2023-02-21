from turtle import *

#we want to paint a house

#step 1: Drawaing a squeare

speed(15)
width(6)
color("blue")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
#end of drawing a squeare 

#drawing a door
left(90)
forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)   #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()
#end of drawing a door

#drawing a rooftop:
penup()
goto(200, 200)
pendown()
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#end of drawing a rooftop

#start of drawing windows

#left window:
penup()
goto(25, 142)
pendown()
color("brown")
begin_fill()
right(150)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()

#right window:
penup()
goto(175, 142)
pendown()
forward(40)
begin_fill()
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()






exitonclick()