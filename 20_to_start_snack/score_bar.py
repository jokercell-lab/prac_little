from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 24, "normal")



class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 360)
        self.write(f"score:{self.score}", align=ALIGN, font=FONT)
        self.hideturtle()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over !!!", align=ALIGN, font=FONT)

    def add_score(self):
        self.clear()
        self.score += 1
        self.write(f"score:{self.score}", align=ALIGN, font=FONT)