import colorgram
import turtle as t
import random

# extract the color from image
# rgb_c = []
# color = colorgram.extract("large.jpg", 30)
# for co in color:
#     r = co.rgb.r
#     g = co.rgb.g
#     b = co.rgb.b
#     new_color = (r, g, b)
#     rgb_c.append(new_color)
#
# print(rgb_c)

color_list = [(235, 246, 250), (251, 241, 246), (243, 235, 74), (211, 158, 93), (186, 12, 69), (112, 179, 208),
              (25, 116, 168), (173, 171, 31), (219, 129, 166), (161, 79, 35), (129, 185, 146), (9, 32, 76),
              (222, 62, 105), (235, 73, 42), (180, 45, 94), (30, 136, 81), (236, 164, 193), (78, 12, 63), (12, 54, 33),
              (234, 227, 7), (26, 165, 209), (16, 43, 132), (58, 166, 96), (134, 214, 229), (10, 101, 63),
              (133, 34, 20), (91, 27, 11), (159, 211, 188)]
color_tuple = tuple(color_list)
tom = t.Turtle()
t.colormode(255)
tom.shape("circle")
tom.speed(1000)
#tom.pensize(10)
tom.setheading(225)
tom.penup()    #一開始拿起來就好了
tom.forward(300)
tom.setheading(0)
num_color = 100
#n = 0
# for _ in range(10):
#     n += 50
#     tom.home()
#     tom.sety(n)
#     for _ in range(10):
#         # tom.color(random.sample(color_tuple, 1))
#         tom.pendown()
#         tom.dot(20, random.choice(color_list))
#         tom.penup()
#         tom.forward(50)

for dot_con in range(1, num_color):
    tom.dot(20, random.choice(color_list))
    #tom.penup()
    tom.forward(50)
    #tom.pendown()
    if dot_con % 10 == 0:
        tom.setheading(90)
        #tom.penup()
        tom.forward(50)
        tom.setheading(180)
        tom.forward(500)
        tom.setheading(0)



screen = t.Screen()
screen.exitonclick()