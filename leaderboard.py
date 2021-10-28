'''
Random appearance of the shape on different parts of the screen
The event of a shape being clicked
The score updating
The timer updating
'''
# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
import leaderboard as lb

#-----game configuration----
xMin = -300
xMax = 300
yMin = -300
yMax = 300
score = 0
timer = 5
timerUp = False
counterInterval = 1000
color = "red"
shape = "triangle"
size = 2
fontSetup = ("Arial", 20, "normal")

leaderboard_file_name = "scores.txt"
leader_names_list = []
leader_scores_list = []
player_name = input("What is your name?")

#-----initialize turtle-----
t = trtl.Turtle()
t.shape(shape)
t.turtlesize(size)
t.fillcolor(color)
t.penup()

scoreWriter = trtl.Turtle()
scoreWriter.penup()
scoreWriter.goto(300,-300)

counter = trtl.Turtle()
counter.penup()
counter.goto(-300, -300)

#-----game functions--------


def spot_clicked(x, y):
    t.goto(rand.randint(xMin,xMax), rand.randint(yMin,yMax))
    scoreChange()

def scoreChange():
    global score
    score += 1
    #print(score)
    scoreWriter.clear()
    scoreWriter.write(score, font=fontSetup)

def countdown():
    global timer, timerUp
    counter.clear()
    if timer <=0:
        counter.write("Time's Up", font=fontSetup)
        timerUp = True
        manage_leaderboard()
    else:
        counter.write("Timer: " + str(timer), font=fontSetup)
        timer -= 1
        counter.getscreen().ontimer(countdown, counterInterval)


# manages the leaderboard for top 5 scorers
def manage_leaderboard():
    global leader_scores_list
    global leader_names_list
    global score
    global spot

    # load all the leaderboard records into the lists
    lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

    # TODO
    if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
        lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
        lb.draw_leaderboard(leader_names_list, leader_scores_list, True, spot, score)

    else:
        lb.draw_leaderboard(leader_names_list, leader_scores_list, False, spot, score)


#-----events----------------
t.onclick(spot_clicked)
wn = trtl.Screen()

wn.ontimer(countdown, counterInterval)
wn.mainloop()