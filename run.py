import turtle
from freegames import vector
from freegames import square
from random import randrange

food = vector(0, 0)
snake = [vector(10, 0)] # [1, 2, 3, 4, 5]
aim = vector(0, -10)

def change_aim(x, y):
    aim.x = x
    aim.y = y

def move():

    head = snake[-1].copy()
    head.move(aim) # forward

    snake.append(head)

    if head == food:
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        print(f'Score : {len(snake) - 1 }')
    else:
        snake.pop(0)
    
    turtle.clear()

    for body in snake:
        square(body.x, body.y, 10, 'red')
    
    square(food.x, food.y, 10, 'blue')
    
    turtle.update()

    turtle.ontimer(move, 100)


turtle.hideturtle()
turtle.tracer(False)

turtle.listen()

turtle.onkey(lambda: change_aim(10, 0), "Right")
turtle.onkey(lambda: change_aim(-10, 0), "Left")
turtle.onkey(lambda: change_aim(0, 10), "Up")
turtle.onkey(lambda: change_aim(0, -10), "Down")

move()

turtle.done()