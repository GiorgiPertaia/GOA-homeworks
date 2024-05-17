from turtle import *

#we want to paint a house

#step 1: draw a square

speed(1)
width(4)
color("green")

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)


#end of square


forward(70)
begin_fill()
color("blue")
left(90)
forward(120) #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(200,200)
pendown()

#end of door

color("black")
begin_fill()
color("purple")
right(150)
forward(200)
left(120)
forward(200)
end_fill()

color("black")

penup()
goto(0,170)
pendown()
left(120)
forward(40)
right(90)
forward(40)
right(90)
forward(40)

#end of left windown
penup()
goto(200,170)
pendown()
forward(40)
left(90)
forward(40)
left(90)
forward(40)
#end of right windown
#drawing crossing for windown one

penup()
goto(0,150)
pendown()
forward(40)
left(90)
forward(20)
left(90)
forward(20)
left(90)
forward(40)

#drawing crossing for windown two

penup()
goto(200,150)
pendown()
right(90)
forward(40)
right(90)
forward(20)
right(90)
forward(20)
right(90)
forward(40)





exitonclick()