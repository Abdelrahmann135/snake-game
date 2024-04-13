from turtle import Turtle


class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.speed("fastest")

    def game_over(self):
        self.write("Game Over", align="center", font=("Courier", 25, "normal"))
