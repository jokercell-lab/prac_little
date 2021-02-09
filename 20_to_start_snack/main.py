from turtle import Turtle, Screen
from snake import Snakesss
import time
from food import Food
from score_bar import Score

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Snake Gamer")
screen.tracer(0)

snake = Snakesss()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.08)
    snake.move()

    #detect
    if snake.head.distance(food) < 15:
        food.renew()
        snake.extend()
        score.add_score()

    #撞到牆
    if snake.head.xcor() > 380 or snake.head.xcor() < -380 or snake.head.ycor() > 380 or snake.head.ycor() < -390:
        game_on = False
        score.game_over()

    #撞到自己
    for body in snake.snake_list[1:]:
        # if body == snake.head:
        #     pass

        if snake.head.distance(body) < 10:
            game_on = False
            score.game_over()





screen.exitonclick()