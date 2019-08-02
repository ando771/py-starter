import turtle

my_turtle = turtle.Turtle()


def draw_square(x0: int, y0: int, width: int):
    """
    Draw square with bottom left angle in x0, y0
    Important: my_turtle should watching to left

    :param x0: int
    :param y0: int
    :param width: int
    """
    my_turtle.penup()
    my_turtle.goto(x0, y0)
    my_turtle.pendown()
    for side in range(4):
        my_turtle.forward(width)
        my_turtle.left(90)


my_turtle.shape('turtle')
initial_x = 0
initial_y = 0
initial_width = 10
step = 10
for time in range(10):
    draw_square(
        initial_x - step * time,
        initial_y - step * time,
        initial_width + step * time * 2
    )

turtle.done()
