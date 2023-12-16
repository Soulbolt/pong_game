from turtle import Turtle, Screen

screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)

paddle = Turtle()
paddle.color("white")
paddle.penup()
paddle.goto(350, 0)
paddle.shape("square")
paddle.shapesize(stretch_len=1, stretch_wid=5)

def move_up():
    new_y = paddle.ycor() + 20
    paddle.goto(350, new_y)


def move_down():
    new_y = paddle.ycor() - 20
    paddle.goto(350, new_y)



screen.listen()
screen.onkey(move_up,"Up")
screen.onkey(move_down,"Down")






screen.exitonclick()
