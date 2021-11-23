'''
1. Random appearance of the shape on different parts of the screen
2. The event of a shape being clicked
3. The score updating
4. The timer updating
'''
# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
#-----game configuration----
xmin = 0
xmax = 112
ymin = 0
ymax = 324
score = 0
timer = 30
timerup = False
counterinterval = 1000
fontsetup = ("Arial", 20, "normal")
color = "red"
shape = "circle"
#size = 2

#-----initialize turtle-----
t = trtl.Turtle()
t.shape(shape)
#t.turtlesize(size)
t.fillcolor(color)
t.penup()
t.hideturtle()

gamestart = trtl.Turtle()
gamestart.penup()
gamestart.goto(50, 0)
gamestart.write("Start", font=fontsetup)

scorewriter = trtl.Turtle()
scorewriter.penup()
scorewriter.goto(400, -350)
scorewriter.hideturtle()

counter = trtl.Turtle()
counter.penup()
counter.goto(-400, -350)
counter.hideturtle()

#-----game functions--------

def spot_clicked(x, y):
    t.goto(rand.randint(xmin, xmax), rand.randint(ymin, ymax))
    scorechange()
    addcolor()
    sizechanger()

def addcolor():
    colorlist = ["black", "blue", "green", "yellow", "lime", "orange", "purple"]
    t.fillcolor(rand.choice(colorlist))
    t.stamp()
    t.fillcolor(color)

def sizechanger():
    sizechange = [0.5, 1, 2, 3, 4, 2.5, 4.8]
    t.turtlesize(rand.choice(sizechange))


def scorechange():
    global score
    score += 1
    scorewriter.clear()
    scorewriter.write(score, font=fontsetup)

def start_game(x, y):
    t.showturtle()
    countdown()
    gamestart.clear
    



def countdown():
    global timer, timerUp
    counter.clear()
    if timer <= 0:
        timer -= 1
        counter.write("time's up", font=fontsetup)
        timerUp = True
    else:
        counter.write("timer: " + str(timer), font=fontsetup)
        timer -= 1
        counter.getscreen().ontimer(countdown, counterinterval)


#-----events----------------
gamestart.onclick(start_game)
t.onclick(spot_clicked)


wn = trtl.Screen()
wn.bgcolor("gray")
wn.mainloop()
