import time
from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)  # Needed along with update and time.sleep using while loop

player_1 = Paddle((-350, 0))
player_2 = Paddle((350, 0))

screen.listen()
screen.onkey(player_1.move_up, "w")
screen.onkey(player_1.move_down, "s")
screen.onkey(player_2.move_up, "Up")
screen.onkey(player_2.move_down, "Down")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    # for dist in range(0, 10, 20):
    #     if player_2.ycor() == 0:
    #         paddle.cpu_move_up()
    # player_2.ycor()
    #
    # for dist in range(0, 10, 20):
    #     if player_2.ycor() > -260 or player_2.ycor() == 260:
    #         paddle.cpu_move_down()
    # player_2.ycor()

screen.exitonclick()
