import sys
import pygame
import os
import turtle
import time
import random
countlength = 0
print("NOTE: Your score is saved when youn lose")
print ("Use W S A D To Move")
blockorblocks = "Block"
turtle.hideturtle()
delay = 0.1
score = 0

# Score
score = 0
setting_data = open('randomfile.txt', 'r')
lines = setting_data.readlines()
limited_n_ints = ''
for i in lines:
  limited_n_ints = limited_n_ints + i
high_score = int(limited_n_ints)

# Set up the screen
wn = turtle.Screen()
wn.title("Snake By Denby Daily")
import tkinter
img = tkinter.Image("photo", file="icon.png")
turtle._Screen._root.iconphoto(True, img)
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0) # Turns off the screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("blue")
food.penup()
food.goto(0,100)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(-1)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

# Functions
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

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main game loop
while True:
    wn.update()

    # Check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        if head.xcor()>290:
            movetox = -290
            movetoy = head.ycor()
            head.goto(movetox,movetoy)
        if head.xcor()<-290:
            movetox = 290
            movetoy = head.ycor()
            head.goto(movetox,movetoy)
        if head.ycor()>290:
            movetox = head.xcor()
            movetoy = -290
            head.goto(movetox,movetoy)
        if head.ycor()<-290:
            movetox = head.xcor()
            movetoy = 290
            head.goto(movetox,movetoy)
        
        
        

    # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("blue")
        new_segment.penup()
        segments.append(new_segment)
        countlength = (countlength) + 1
        print ("Yummy!")
        if countlength > 1:
            blockorblocks = "Blocks"
        print ("You are now", countlength, blockorblocks, "long.")


        # Shorten the delay
        delay -=0.001

        # Increase the score
        score += 10



        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
        

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()
    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            print("YOU DIED!")
            os.system("attrib -s -h randomfile.txt")
            print(high_score, file=open("randomfile.txt", "w"))
            os.system("attrib +s +h randomfile.txt")
            os.system("pause")
            print("Go back to your game")


            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1

            # Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))


    

    time.sleep(delay)

wn.mainloop()
exit()
