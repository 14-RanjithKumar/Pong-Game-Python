import turtle

score_a = 0
score_b = 0
# window creation
win = turtle.Screen()
win.setup(800, 600)
win.bgcolor("green")  # set a background color of the window
win.title("Pong Game")
win.tracer(0)  # To stop the trace from one point to another

# left paddle
left_paddle = turtle.Turtle()  # To draw a shapes
left_paddle.shape("square")  # To create a square shape
left_paddle.color("Yellow")  # To set the color of the square
left_paddle.shapesize(stretch_wid=5, stretch_len=1)  # To set the size of the paddle left
left_paddle.speed(0)  # To fix the paddle at particular position
left_paddle.penup()  # To hide the drawing
left_paddle.goto(-390, 0)  # To set the position of the paddle left

# right paddle
right_paddle = turtle.Turtle()  # To draw a shapes
right_paddle.shape("square")  # To create a square shape
right_paddle.color("Yellow")  # To set the color of the square
right_paddle.shapesize(stretch_wid=5, stretch_len=1)  # To set the size of the paddle right
right_paddle.speed(0)  # To fix the paddle at particular position
right_paddle.penup()  # To hide the drawing
right_paddle.goto(380, 0)  # To set the position of the paddle right

# ball
ball = turtle.Turtle()  # To assign the new turtle
ball.speed(0)  # To fix the ball at a particular position
ball.shape("circle")  # Set the shape as circle
ball.color("red")  # set the color as red
ball.penup()
ball.dx = 0.3
ball.dy = 0.3

# scores
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.speed(0)
pen.penup()
pen.goto(0, 260)
pen.hideturtle()
pen.write("Player A: 0  Player B: 0", align="center", font=("Ariel", 24, "normal"))


# moving paddles
def left_paddle_up():
    left_paddle.sety(left_paddle.ycor() + 20)  # To move the paddle 20px up by clicking the w button


def left_paddle_down():
    left_paddle.sety(left_paddle.ycor() - 20)
    # To move the paddle 20px down by clicking the s button


def right_paddle_up():
    right_paddle.sety(right_paddle.ycor() + 20)  # To move the paddle 20px up by clicking the up button


def right_paddle_down():
    right_paddle.sety(right_paddle.ycor() - 20)
    # To move the paddle 20px down by clicking the down button


win.listen()  # which is listening the operation of the key to pressed by the user

win.onkeypress(left_paddle_up, "w")
win.onkeypress(left_paddle_down, "s")
win.onkeypress(right_paddle_up, "Up")
win.onkeypress(right_paddle_down, "Down")

while True:
    win.update()  # To display the screen continuously
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # top wall
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    # bottom wall
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # right wall
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Ariel", 24, "normal"))

    # left wall
    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Ariel", 24, "normal"))
    # collision with paddles
    # if ball.xcor() > 370 and right_paddle.ycor() + 50 and right_paddle.ycor() - 50:
    #     ball.dx *= -1
    #
    # if ball.xcor() < -370 and left_paddle.ycor() + 50 and left_paddle.ycor() - 50:
    #     ball.dx *= -1

    if ball.xcor() > 370 and right_paddle.ycor()-50<ball.ycor()<right_paddle.ycor()+50:
        ball.setx(360)
        ball.dx *= -1
    if ball.xcor() < -370 and left_paddle.ycor()-50<ball.ycor()<left_paddle.ycor()+50:
        ball.setx(-360)
        ball.dx *= -1