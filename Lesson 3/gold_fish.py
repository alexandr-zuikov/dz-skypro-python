from turtle import *

body_color = "orange"
eye_color = "white"

my_turtle = Turtle()
my_turtle.speed(10)
my_turtle.screen.setup(1300,1200)
my_turtle.screen.bgcolor("skyblue")

def body():
	my_turtle.pensize(10)
	my_turtle.fillcolor(body_color)
	my_turtle.begin_fill()
	my_turtle.circle(135,130)
	my_turtle.circle(-90,75)
	my_turtle.left(90)
	my_turtle.forward(120)
	my_turtle.right(70)
	my_turtle.circle(90,-75)
	my_turtle.circle(90,-75)
	my_turtle.circle(-180,-150)
	my_turtle.right(130)
	my_turtle.forward(130)
	my_turtle.circle(130,150)
	my_turtle.right(160)
	my_turtle.forward(200)
	my_turtle.right(90)
	my_turtle.forward(100)
	my_turtle.circle(10,100)
	my_turtle.left(45)
	my_turtle.circle(180,40)
	my_turtle.right(90)
	my_turtle.forward(160)
	my_turtle.left(150)
	my_turtle.circle(-180,30)
	my_turtle.left(50)
	my_turtle.circle(160,-42)
	my_turtle.left(-10)
	my_turtle.end_fill()
	
def line():
	my_turtle.pensize(10)
	my_turtle.fillcolor(body_color)
	my_turtle.begin_fill()
	my_turtle.up()
	my_turtle.forward(120)
	my_turtle.down()
	my_turtle.end_fill()
	
def eye():
	my_turtle.pensize(10)
	my_turtle.fillcolor(eye_color)
	my_turtle.begin_fill()
	my_turtle.circle(30)
	my_turtle.left(90)
	my_turtle.up()
	my_turtle.forward(20)
	my_turtle.end_fill()

def icon():
	my_turtle.down()
	my_turtle.pensize(10)
	my_turtle.circle(10)


body()
line()
eye()
icon()

my_turtle.screen.exitonclick()
my_turtle.screen.mainloop()