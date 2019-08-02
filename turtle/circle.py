import turtle

my_turtle = turtle.Turtle()

my_turtle.shape('turtle')
my_turtle.penup()
my_turtle.goto(50, 50)
my_turtle.pendown()
my_turtle.left(90)
for angle in range(360):
    my_turtle.forward(1)
    my_turtle.left(1)

turtle.done()
