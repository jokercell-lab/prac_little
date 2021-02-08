from turtle import Turtle, Screen
import random


game_start = False
screen = Screen()
screen.setup(width=500, height=400)
user = screen.textinput(title="choose a turtle", prompt="which on ?")
colors = ["red", "blue", "purple", "yellow", "green", "orange"]
y_sit = [-70, -40, -10, 20, 50, 80]
all_turtle = []
# tom0 = Turtle(shape="turtle")
# tom1 = Turtle(shape="turtle")
# tom2 = Turtle(shape="turtle")
# tom3 = Turtle(shape="turtle")
# tom4 = Turtle(shape="turtle")
# tom5 = Turtle(shape="turtle")
# turtle_tuple = (tom0, tom1, tom2, tom3, tom4, tom5)
#
# n = -1
# y1 = 0
# for tom in turtle_tuple:
#     n += 1
#     tom.color(colors[n])
#     tom.penup()
#     y1 += 30
#     tom.goto(x=-220, y=-100 + y1)
for turtle_index in range(0, 6):
    tom = Turtle(shape="turtle")
    tom.color(colors[turtle_index])
    tom.penup()
    tom.goto(x=-220, y=y_sit[turtle_index])
    all_turtle.append(tom)

if user:
    game_start = True

while game_start:
    for turtle in all_turtle:
        if turtle.xcor() > 200:
            game_start = False
            win_color = turtle.pencolor()
            if win_color == user:
                print(f"you win!!! {win_color} run fastest!")
            else:
                print(f"you lose, the final is {win_color}")
        random_run = random.randint(1,10)
        turtle.forward(random_run)


screen.exitonclick()