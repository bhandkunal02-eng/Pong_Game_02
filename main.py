from turtle import Turtle ,Screen
from Paddle import Paddle
from Ball import Ball
from score_board import Scoreboard
import time
screen=Screen()
screen.tracer(0)
scoreboard=Scoreboard()

screen.title("Pong Game")
screen.bgcolor("Black")
screen.setup(800,600)


r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()







screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() <-280 :
        # We need to bounce the ball. from wall
        ball.bounce_y()
    
    # bounce   ball form rif=ght paddle 
    if ball.distance(r_paddle) <50 and ball.xcor()> 325 :
        ball.bounce_x()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -325:
        ball.bounce_x()

    # right side paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # left side paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()



    

    















screen.exitonclick()