from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#you can change the duration of the game from here
DURATION = 60*1    # 1 min

#create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("ping-pong")
screen.tracer(0)

#create the paddles and the scoreboard
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

#move the right paddle using the up & down keys
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
#move the right paddle using the w & s keys
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

#one game lasts for the duration of 1min
timeout = time.time() + DURATION
game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.time_sleep)

    # detect collision with top/bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with right paddle
    if ball.xcor() > 320 and ball.distance(r_paddle) < 55:
        ball.bounce_x()
        score.r_point()

    # detect collision with left paddle
    if ball.xcor() < -320 and ball.distance(l_paddle) < 55:
        ball.bounce_x()
        score.l_point()

    # detect when r_paddle misses
    if ball.xcor() > 360:
        ball.reset()
        score.l_point()
    # detect when l_paddle misses
    if ball.xcor() < -360:
        ball.reset()
        score.r_point()

    if time.time() > timeout:
        game_is_on = False
        score.game_over()


screen.exitonclick()
