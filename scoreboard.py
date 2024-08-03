from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 40, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.hideturtle()
        self.goto(0, 300)
        for i in range(1, 11):
            self.setheading(270)
            self.pendown()
            self.forward(30)
            self.penup()
            self.forward(30)
        self.update()

    def update(self):
        self.clear()
        self.goto(100, 200)
        self.write(arg=f"{self.r_score}", align=ALIGNMENT, font=FONT)
        self.goto(-100, 200)
        self.write(arg=f"{self.l_score}", align=ALIGNMENT, font=FONT)

    def r_point(self):
        self.r_score += 1
        self.update()

    def l_point(self):
        self.l_score += 1
        self.update()

    def game_over(self):
        self.write("TIME'S UP!!!")