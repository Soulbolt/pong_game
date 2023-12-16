import random
from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    # def cpu_move_up(self):
    #     intervals = 0
    #     new_y = self.player_two.ycor()
    #     # if self.player_two.ycor() == 0 and self.player_two.ycor() < 240:
    #     intervals += 20
    #     self.player_two.goto(self.player_two.xcor(), new_y + intervals)
    #
    # def cpu_move_down(self):
    #     intervals = 0
    #     new_y = self.player_two.ycor()
    #     # if self.player_two.ycor() > -240:
    #     intervals += 20
    #     self.player_two.goto(self.player_two.xcor(), new_y - intervals)
