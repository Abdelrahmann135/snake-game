from turtle import Turtle
POSITION_LIST = [(0, 0), (-20, 0), (-40, 0)]
SNAKE_STEPS = 20


class Snake:

    def __init__(self):
        self.snakes_list = []
        self.make_snake()
        self.head = self.snakes_list[0]

    def make_snake(self):
        for ind in POSITION_LIST:
            snake = Turtle(shape="square")
            snake.color("white")
            snake.penup()
            snake.goto(ind)
            self.snakes_list.append(snake)

    def move(self):
        for snake in range(len(self.snakes_list) - 1, 0, -1):
            x = self.snakes_list[snake - 1].xcor()
            y = self.snakes_list[snake - 1].ycor()
            self.snakes_list[snake].goto(x=x, y=y)
        self.head.forward(SNAKE_STEPS)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def check_wall(self):
        if self.head.xcor() > 280 or self.head.xcor() < -280 or self.head.ycor() > 280 or self.head.ycor() < -280:
            return True

    def check_tail(self):
        for part in self.snakes_list[1:]:
            if self.head.distance(part) < 5:
                return True

    def increase_snake(self):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(self.snakes_list[-1].pos())
        self.snakes_list.append(snake)
