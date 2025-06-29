from turtle import*


#we want to paint a house 

#step1: draw a square 
speed(30)
width(7)
color("blue")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square 

#drawing a door 
forward(70)
color("yellow")

left(90)
forward(120)   #height of door
right(90)
forward(60)
right(90)
forward(120)


penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill

color("purple")
penup()
goto(180,180)
pendown()
begin_fill()
right(60)   #draw a line
forward(35)
left(90)

forward(35)
left(90)

forward(35)
left(90)

forward(35)
left(90)
end_fill()


penup()
goto(30,145)
pendown()
begin_fill()
right(90)
forward(35)

right(90)
forward(35)

right(90)
forward(35)

right(90)
forward(35)
end_fill()


penup()







exitonclick()