from turtle import Screen
from end_game import GameOver
from food import Food
from scoe import ScoreBoard
from snake import Snake
import time
snake = Snake()
screen = Screen()
food = Food()
score = ScoreBoard()
end = GameOver()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
keep_going = True
while keep_going:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        score.update_score()
        snake.increase_snake()
    if snake.check_wall() or snake.check_tail():
        keep_going = 0
        end.game_over()

screen.exitonclick()
