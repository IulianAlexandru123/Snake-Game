import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

#Setting up the screen

wn = turtle.Screen()
wn.title("Snake Game by IulianAlexandru")
wn.bgcolor("black")
#wn.bgpic("fundal.gif")
wn.setup(width = 600, height = 600)
wn.tracer(0)

#Create Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"

#Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(100,100)

segments = []

#Scoring
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: 0", align = "center", font = ("Courier", 24, "normal"))

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_right, "d")

while True:
    wn.update()

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        for segment in segments:
            segment.goto(1000,1000)

        segments.clear()

        score = 0

        delay = 0.1

        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    if head.distance(food) < 20:
        food.goto(random.randint(-290,290), random.randint(-290,290))

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        delay -= 0.001

        score += 10

        if(score > high_score):
            high_score = score
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align = "center", font = ("Courier", 24, "normal"))

    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

            for segment in segments:
                segment.goto(1000, 1000)

            segments.clear()

    time.sleep(delay)


wn.mainloop()