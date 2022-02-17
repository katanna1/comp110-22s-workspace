"""TODO: Describe your scene program."""

__author__ = "Your PID"

from turtle import Turtle, colormode, done 
leo: Turtle = Turtle()
colormode(255)


def main() -> None:
    """The entrypoint of my scene."""
    # TODO: Declare your Turtle variable(s) here.
    # TODO: Call the procedures you define and pass your Turtle(s) as an argument.
    done()

# TODO: Define the procedures for other components in your scene here.

# TODO: Use the __name__ is "__main__" idiom shown in 


leo.begin_fill()


def draw_mountain(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw a triangle of the given width """
    a_turtle.penup()
    a_turtle.goto(x, y) 
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    leo.pencolor("brown")
    leo.fillcolor(75, 22, 11)
    i: int = 0
    while (i < 3):
        leo.forward(200)
        leo.left(120)
        i = i + 1


draw_mountain(leo, 0, 0, 10)
draw_mountain(leo, 50, 0, 10)


leo.end_fill()


leo.penup()
leo.goto(30, 70)


def draw_snow(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw a curvy line of the given length """
    leo.pencolor("white")
    a_turtle.setheading(0.0)
    i: int = 0
    while (i < 5):
        leo.pendown()
        leo.left(45)
        leo.forward(20)
        leo.right(45)
        leo.forward(20)
        i = i + 1
        leo.penup()


draw_snow(leo, 30, 10, 5)    


def draw_valley(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw a green rectangle for the picture."""
    leo.pencolor("green")
    a_turtle.penup()
    a_turtle.setheading(0.0)
    a_turtle.goto(-100, -100) 
    i: int = 0
    while (i < 2):
        leo.pendown()
        leo.left(270)
        leo.backward(100)
        leo.left(270)
        leo.backward(500)
        i = i + 1
        leo.penup()


draw_valley(leo, 0, 0, 360)    


# i: int = 0
# while (i < 3):
#     leo.forward(300)
#     leo.left(120)
#     i = i + 1

leo.color("blue")
colormode(255)
leo.color(99, 204, 250)

leo.begin_fill()
# code for shape to be filled 
leo.end_fill()

leo.pencolor("pink")
leo.fillcolor(32, 30, 93)
leo.color("green", "yellow")

leo.speed(30)
leo.hideturtle()
