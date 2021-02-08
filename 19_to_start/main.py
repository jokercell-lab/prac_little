from turtle import Turtle, Screen

tom = Turtle()
screen = Screen()


def move_forwards():
    tom.forward(10)


def move_back():
    tom.backward(10)


def angle_adjust_r():
    new1 = tom.heading() - 5
    tom.setheading(new1)


def angle_adjust_l():
    new = tom.heading() + 5
    tom.setheading(new)


def clear():
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()


screen.listen()

screen.onkey(move_forwards, "w")
screen.onkey(lambda: move_back(), "s")
screen.onkey(lambda: angle_adjust_l(), "a")
screen.onkey(lambda: angle_adjust_r(), "d")
screen.onkey(lambda: clear(), "c")

screen.exitonclick()


