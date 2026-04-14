import turtle
import winsound

win = turtle.Screen()
win.title("Mr Pz Ping Pong & Bong")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

#Score
Score_a = 0
Score_b = 0


#Paddle A
PadA = turtle.Turtle()
PadA.speed(0)
PadA.shape("square")
PadA.color("blue")
PadA.shapesize(stretch_wid=5, stretch_len=1)
PadA.penup()
PadA.goto(-350, 0)

#Paddle B
PadB = turtle.Turtle()
PadB.speed(0)
PadB.shape("square")
PadB.color("red")
PadB.shapesize(stretch_wid=5, stretch_len=1)
PadB.penup()
PadB.goto(350, 0)

#Ball
Ball = turtle.Turtle()
Ball.speed(0)
Ball.shape("circle")
Ball.color("white")
Ball.shapesize(stretch_wid=1, stretch_len=1)
Ball.penup()
Ball.goto(0, 0)
Ball.dx = 0.25
Ball.dy = 0.25

#Pen
Pen = turtle.Turtle()
Pen.speed(0)
Pen.color("white")
Pen.penup()
Pen.hideturtle()
Pen.goto(0, 260)
Pen.write("Player A: {}  Player B: {}".format(Score_a, Score_b), align="center", font=("Courier", 24, "normal"))


#Functions
#Paddle A
def PA_Up():
    y= PadA.ycor()
    y+= 20
    PadA.sety(y)
    
def PA_Down():
    y= PadA.ycor()
    y-= 20
    PadA.sety(y)    

#Paddle B
def PB_Up():
    y= PadB.ycor()
    y+= 20
    PadB.sety(y)
    
def PB_Down():
    y= PadB.ycor()
    y-= 20
    PadB.sety(y)  

#Keyboard Binding
win.listen()
win.onkeypress(PA_Up, "w")
win.onkeypress(PA_Down, "s")
win.onkeypress(PB_Up, "Up")
win.onkeypress(PB_Down, "Down")



#Main Game Loop
while True:
    win.update()
    
    #Moving Ball
    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)
    
    #Boarder Checking
    if Ball.ycor() > 290:
        Ball.sety(290)
        Ball.dy *= -1
        winsound.PlaySound("", winsound.SND_ASYNC)
    
    if Ball.ycor() < -290:
        Ball.sety(-290)
        Ball.dy *= -1
        winsound.PlaySound("", winsound.SND_ASYNC)
    
    if Ball.xcor() > 390:
        Ball.goto(0, 0)
        Ball.dx *= -1
        Score_a += 1
        Pen.clear()
        Pen.write("Player A: {}  Player B: {}".format(Score_a, Score_b), align="center", font=("Courier", 24, " normal"))
    
    if Ball.xcor() < -390:
        Ball.goto(0, 0)
        Ball.dx *= -1
        Score_b += 1
        Pen.clear()
        Pen.write("Player A: {}  Player B: {}".format(Score_a, Score_b), align="center", font=("Courier", 24, " normal"))
    
    
    #Collisions A
    if Ball.xcor() < -340 and Ball.xcor() > -350 and Ball.ycor() < PadA.ycor()+40 and Ball.ycor() > PadA.ycor()-40 :
        Ball.setx(-340)
        Ball.dx *= -1
        winsound.PlaySound("", winsound.SND_ASYNC)
    
    #Collisions B
    if Ball.xcor() > 340 and Ball.xcor() < 350 and Ball.ycor() < PadB.ycor()+40 and Ball.ycor() > PadB.ycor()-40 :
        Ball.setx(340)
        Ball.dx *= -1
        winsound.PlaySound("", winsound.SND_ASYNC)
    