"""A pretty mountain scene on a sunny day."""

__author__ = "730479768"

from turtle import Turtle, colormode, done 
leo: Turtle = Turtle()
colormode(255)


leo.begin_fill()


def draw_mountain(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw 2 brown triangles of the given width, drawing mountains."""
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
    """Draw a white curvy line of the given length, to draw a snow cap."""
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


leo.begin_fill()


def draw_valley(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw a green rectangle of the given width, to draw a valley."""
    leo.pencolor("green")
    leo.fillcolor(25, 182, 45)
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


leo.end_fill()

leo.begin_fill()


def draw_sun(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw a yellow circle for the picture, to make a sun."""
    leo.pencolor("yellow")
    leo.fillcolor(215, 209, 47)
    a_turtle.penup()
    a_turtle.setheading(0.0)
    a_turtle.goto(-100, 100) 
    i: int = 0
    while (i < 2):
        leo.pendown()
        leo.circle(50)
        i = i + 1
        leo.penup()


draw_sun(leo, 0, 0, 360)    


leo.end_fill()