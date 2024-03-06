from turtle import Screen
from day_87_ball import Ball
from day_87_paddle import Paddle
from day_87_scoreboard import ScoreBoard
from day_87_blocks import BlockManger
import time

screen = Screen()
screen.setup(width=500, height= 600)
screen.bgcolor("black")
screen.title("Breakout Game")
screen.tracer(0)

paddle = Paddle((0,-260))
ball = Ball()
scoreboard = ScoreBoard()
block_manager = BlockManger()

screen.listen()
screen.onkeypress(paddle.go_right, "Right")
screen.onkeypress(paddle.go_left, "Left")

game_in_on = True
while game_in_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)


#detect collidion with wall.
    if ball.xcor() > 220 or ball.xcor() < -230:
        ball.bounce_x()
        
#detect collidion with paddle and upper wall.        
    if (ball.ycor() < -227 and ball.distance(paddle) < 55) or (ball.ycor() > 270) : 
        ball.bounce_y() 
        
        
    if ball.ycor() < -300:
        ball.reset_position()
        scoreboard.lose_life()
        
        
    # Detect collision with blocks
    for block in block_manager.all_blocks:
        if ball.distance(block) < 33:
            ball.bounce_y()
            block_manager.remove_blocks(block)
            scoreboard.give_score()
    #playyer won by destroying all blocks
    if scoreboard.score == 27:
        scoreboard.win()
        game_in_on = False
    # playyer lose by losing all life
    if scoreboard.lives < 1:
        scoreboard.lose()
        game_in_on = False   
        
                        




screen.exitonclick()