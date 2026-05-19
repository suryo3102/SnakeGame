from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
MOVE_SPEED = 150 
STEP_SIZE = 20
CELL_SIZE = 18
BOARD_LIMIT = 300

snake = [vector(20, 0)]
aim = vector(0, -STEP_SIZE)


BG_COLOR = '#08111F'
SNAKE_COLOR = '#00F5D4'
FOOD_COLOR = '#FF4D8D'
GRID_COLOR = '#1B3A57'
SCORE_COLOR = '#FFFFFF'

score_pen = Turtle(visible=False)
score_pen.penup()
score_pen.color(SCORE_COLOR)
score_pen.speed(0)

def draw_grid():
    "Draw a subtle grid pattern in the background."
    penup()
    pencolor(GRID_COLOR)
    for x in range(-BOARD_LIMIT, BOARD_LIMIT + 1, STEP_SIZE):
        goto(x, -BOARD_LIMIT)
        pendown()
        goto(x, BOARD_LIMIT)
        penup()
    for y in range(-BOARD_LIMIT, BOARD_LIMIT + 1, STEP_SIZE):
        goto(-BOARD_LIMIT, y)
        pendown()
        goto(BOARD_LIMIT, y)
        penup()

def change(x, y):
    "Change snake direction."

    if (aim.x != -x) and (aim.y != -y):
        aim.x = x
        aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -BOARD_LIMIT < head.x < BOARD_LIMIT - STEP_SIZE and -BOARD_LIMIT < head.y < BOARD_LIMIT - STEP_SIZE

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)


    if not inside(head) or head in snake:
        game_over()
        return

    snake.append(head)

    if head == food:
        print('Snake Length:', len(snake))
        food.x = randrange(-(BOARD_LIMIT // STEP_SIZE) + 1, BOARD_LIMIT // STEP_SIZE) * STEP_SIZE
        food.y = randrange(-(BOARD_LIMIT // STEP_SIZE) + 1, BOARD_LIMIT // STEP_SIZE) * STEP_SIZE
    else:
        snake.pop(0)

    clear()

    bgcolor(BG_COLOR)
    draw_grid()

    for i, body in enumerate(snake):
        square(body.x, body.y, CELL_SIZE, SNAKE_COLOR)

    square(food.x, food.y, CELL_SIZE, FOOD_COLOR)

    score_pen.clear()
    score_pen.goto(-BOARD_LIMIT + 12, BOARD_LIMIT + 18)
    score_pen.write(f'Score: {len(snake) - 1}', font=('Arial', 18, 'bold'))

    update()
    ontimer(move, MOVE_SPEED)

def game_over():
    "Display game over message and exit gracefully."
    square(snake[-1].x, snake[-1].y, CELL_SIZE, '#FF2E63')
    update()
    print('Game Over! Your final score:', len(snake))
    bye() 


setup(720, 720, 240, 0)
hideturtle()
tracer(False)
listen()


title("Snakemania")


onkey(lambda: change(STEP_SIZE, 0), 'Right')
onkey(lambda: change(-STEP_SIZE, 0), 'Left')
onkey(lambda: change(0, STEP_SIZE), 'Up')
onkey(lambda: change(0, -STEP_SIZE), 'Down')


move()

done()
