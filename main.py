from turtle import Turtle, Screen

paddle = Turtle()
paddle.color("white")
paddle.penup()
paddle.goto(-780,0)
paddle.shape("square")
paddle.shapesize(stretch_len=1, stretch_wid=5)

screen = Screen()
screen.bgcolor("black")
screen.screensize(canvwidth=800, canvheight=600)


def move_up():
    paddle.setheading(90)


screen.listen()






screen.exitonclick()
