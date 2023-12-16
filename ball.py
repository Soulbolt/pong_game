from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        # self.goto(350, 400)

    def move(self):
        self.setheading(25)
        self.goto(self.xcor() + 25, self.ycor() + 20)

