from turtle import Turtle, Screen


START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIS = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snakesss:
    def __init__(self):
        self.snake_list = []
        self.position()
        self.head = self.snake_list[0]

    def position(self):
        for posit in START_POSITION:
            self.add_snake(posit)

    def add_snake(self, posit):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(posit)
        self.snake_list.append(snake)

    def extend(self):
        self.add_snake(self.snake_list[-1].position())

    def move(self):
        for snk_num in range(len(self.snake_list) - 1, 0, -1):
            new_x = self.snake_list[snk_num - 1].xcor()
            new_y = self.snake_list[snk_num - 1].ycor()
            self.snake_list[snk_num].goto(new_x, new_y)
        self.snake_list[0].forward(MOVE_DIS)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)