import random
from turtle import Turtle

# CONSTANTS
STARTING_POSITIONS = [(350, 0), (-350, 0)]


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.paddle_count = []
        self.create_paddle()
        self.player_one = self.paddle_count[0]
        self.player_two = self.paddle_count[1]

    def create_paddle(self):
        for location in STARTING_POSITIONS:
            self.add_paddle(location)

    def add_paddle(self, location):
        new_paddle = Turtle(shape="square")
        new_paddle.shapesize(stretch_len=1, stretch_wid=5)
        new_paddle.penup()
        new_paddle.color("white")
        new_paddle.goto(location)
        self.paddle_count.append(new_paddle)

    def move_up(self):
        new_y = self.player_one.ycor() + 20
        self.player_one.goto(self.player_one.xcor(), new_y)

    def move_down(self):
        new_y = self.player_one.ycor() - 20
        self.player_one.goto(self.player_one.xcor(), new_y)

    def cpu_move_up(self):
        intervals = 0
        new_y = self.player_two.ycor()
        # if self.player_two.ycor() == 0 and self.player_two.ycor() < 240:
        intervals += 20
        self.player_two.goto(self.player_two.xcor(), new_y + intervals)

    def cpu_move_down(self):
        intervals = 0
        new_y = self.player_two.ycor()
        # if self.player_two.ycor() > -240:
        intervals += 20
        self.player_two.goto(self.player_two.xcor(), new_y - intervals)
