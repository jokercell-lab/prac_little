import turtle as t
import random

tommy = t.Turtle()
t.colormode(255)

def change_color():
    r = random.randint(0, 230)
    g = random.randint(0, 230)
    b = random.randint(0, 230)
    RGB = (r, g, b)
    return RGB

tommy.shape("circle")
tommy.shapesize(stretch_wid=0.5, stretch_len=0.5, outline=0.5)
tommy.speed(1000)
# tommy.pensize(5)


def circle_draw(angel, radious):
    for _ in range(round(360 / angel)):
        tommy.color(change_color())
        tommy.right(angel)
        tommy.circle(radious)


circle_draw(3, 150)


# angle = [0, 90, 180, 270]
# # for _ in range(1000):
# #     tommy.color(change_color())
# #     tommy.right(random.choice(angle))
# #     tommy.forward(20)
#
#
#
# for _ in range(1000):
#     tommy.color(change_color())
#     tommy.right(random.randint(0, 360))
#     tommy.forward(20)
#     # R = random.random()
#     # G = random.random()
#     # B = random.random()
#     # tommy.color(R, G, B)


screen = t.Screen()
screen.exitonclick()
