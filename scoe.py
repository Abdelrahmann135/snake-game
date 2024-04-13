from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(-10, 250)
        self.speed("fastest")
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Your Score: {self.score}", align="center", font=("Courier", 20, "normal"))
        self.score += 1
