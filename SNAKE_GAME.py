#make screen
#part 2:snake head
#make a food
import time
import turtle
import random

delay=0.1
score=0
high_score=0
#set the screen
wn=turtle.Screen()
wn.title("SNAKE GAME")
wn.bgcolor("green")
wn.setup(width=600,height=600)
wn.tracer(0) #turns off the screen updates

#snake head
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction="stop"

#snake food
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments=[]

#pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0   High score: 0",align="center",font=("Courier",24,"normal"))


#functions
def go_up():
    if head.direction!="down":
        head.direction="up"
def go_down():
    if head.direction != "up":
        head.direction="down"
def go_right():
    if head.direction != "left":
        head.direction="right"
def go_left():
    if head.direction !="right":
        head.direction="left"

def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)

    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)

    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)

    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)

#keyboard bindings
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_right,"d")
wn.onkeypress(go_left,"a")

#MAIN GAME LOOP

while True:
    wn.update()
    #check for a collision with border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()<-290 or head.ycor()>290:
        time.sleep(1)
        head.goto(0,0)
        head.direction='stop'
#hidde the segment
        for segment in segments:
            segment.goto(1000,1000)

#clear the dsegment list
        segments.clear()
        #reset the score
        score=0
        #reset the delay
        delay=0.1
        pen.clear()
        pen.write("score: {}   High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    #check for colloison with the food
    if head.distance(food)<20:
        #move the food to a random spot
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)
        #add a segment
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("purple")
        new_segment.penup()
        segments.append(new_segment)

        #shorten the delay
        delay-=0.001

        #increase the score
        score+=10
        if score>high_score:
            high_score=score
        pen.clear()
        pen.write("score: {}   High Score: {}".format(score,high_score),align="center",font=("Courier",24,"normal"))

    #move the end segments first in reverse order
    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)

    #move segment 0 to where the heaad is
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)

    move()

    #check for head collision with the body segments
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.direction="stop"
            #hide the segment
            for segment in segments:
                segment.goto(1000,1000)

            #clear the segment list
            segment.clear()
            # reset the score
            score = 0
            #reset the delay
            delay=0.1
            #update the score display
            pen.clear()
            pen.write("score: {}   High Score: {}".format(score, high_score), align="center",font=("Courier", 24, "normal"))

    time.sleep(delay)



wn.mainloop()