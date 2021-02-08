# import turtle
# tommy = turtle.Turtle()
#
# from turtle import Turtle, Screen
#
# tommy = Turtle()
# tommy.shape("turtle")
# tommy.color("coral")
# tommy.forward(100)
# m_screen = Screen()
# print(m_screen.canvwidth)
# m_screen.exitonclick()


from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Fruit", ["apple", "banana", "Custard", "VonDan"], "c", "t")
table.add_column("Type", ["water", "fire", "electric", "tree"], "c", "t")
table.align = "l"

print(table)