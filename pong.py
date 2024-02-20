#Pong Game using turtule module in python
import turtle
import os

wn = turtle.Screen()
wn.title("pong by CS-astronaut")
wn.bgcolor("black")
wn.setup(width=800, height=600)

wn.tracer(0) #stops the window from updating

#score
score_a = 0
score_b = 0


# baddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #set the speed to the maximum speed
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("white")
paddle_a.penup() #we dont need to draw lines
paddle_a.goto(-350, 0)


# baddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) #set the speed to the maximum speed
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")
paddle_b.penup() #we dont need to draw lines
paddle_b.goto(350, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0) #set the speed to the maximum speed
ball = turtle.Turtle()
ball.shape("square")
ball.color("white")
ball.penup() #we dont need to draw lines
ball.goto(0, 0)

# Ball movements
ball.dx = 0.1
ball.dy = 0.1

# pen 
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write(f"Player A:0 Player B:0" , align="center", font=("Courier", 15, "normal"))

# Fucntion
def paddle_a_up():
    y = paddle_a.ycor()
    y += 25
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 25
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 25
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 25
    paddle_b.sety(y)

#keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_b_up, "Up")

wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_down, "Down")


# main game loop
while True:
    wn.update()

    # move the ball 
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("aplay bounce.wav&")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1   
        os.system("aplay bounce.wav&")

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A:{} Player B:{}".format(score_a,score_b) , align="center", font=("Courier", 15, "normal"))
        os.system("aplay bounce.wav&")

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A:{} Player B:{}".format(score_a,score_b) , align="center", font=("Courier", 15, "normal"))
        os.system("aplay bounce.wav&")


    # paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350 ) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        os.system("aplay bounce.wav&")

    if (ball.xcor() < -340 and ball.xcor() > -350 ) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        os.system("aplay bounce.wav&")
