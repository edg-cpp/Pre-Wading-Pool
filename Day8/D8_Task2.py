import turtle
import random

#### 2
'''
toto = turtle.Screen() #on ouvre le'écran
toto.bgcolor("black") #backround color is black
titi = turtle.Turtle() #crée un objet
titi.color("red") #objet sera rouge
for i in range(3):
    titi.right(90) #tourne 90 deg à droite
    titi.circle(42) #crée un cercle de 42 ppixels de rayon
toto.exitonclick() #on ferme l'écran
'''

#### 3
def draw_polygon(sides):
    scr = turtle.Screen() #on ouvre le'écran
    scr.bgcolor("white")
    polygone = turtle.Turtle()
    polygone.color("blue")
    polygone.circle(100,steps=sides)
    scr.exitonclick()
    
#draw_polygon(5)

### 4
def spiral():
    scr = turtle.Screen() #on ouvre le'écran
    scr.bgcolor("white")

    sp = turtle.Turtle()
    sp.color("black")
    for i in range (10,500,10):
        sp.circle(i,extent=60)
    scr.exitonclick()

#spiral()

### Challenge

def ch2():
    scr = turtle.Screen() #on ouvre l'écran
    scr.bgcolor("white")
    obj=turtle.Turtle()
    obj.speed(0)
    turtle.colormode(255)
    for i in range(100,10,-10):
        for j in range(18):
            obj.begin_fill()
            obj.circle(i,steps=4)
            obj.fillcolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
            obj.right(20)
            obj.end_fill()
    scr.exitonclick()
#ch2()
# à voir si c'est refaisable avec d'autres modules de turtle

def ch1():
    scr = turtle.Screen() #on ouvre l'écran
    scr.bgcolor("white")
    turtle.color('#ff00ff')
    turtle.speed(0)
    for j in range(19):
            turtle.circle(15,extent=180)
            turtle.circle(100,extent=90)
            turtle.right(5)
    scr.exitonclick()

ch1()