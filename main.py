
from const import *
import random
from turtle import *

window = Screen()
window.title("Sierpinski Triangle")
window.setup(1000,1000)
window.tracer(0,0)
hideturtle()
speed(0)
penup()

for i in V:
    goto(i)
    dot("red")


n = 2       #number of generated points (increase for clearer pic)
p = (random.uniform(-200,200), random.uniform(-200,200))        #random starting point
# p = (0,0)

t = Turtle()
t.up()
t.hideturtle()

for i in range(n):
    t.goto(p)
    t.dot(4,"blue")

    r = random.randrange(len(V))        #pick a random vertex
    p = ((V[r][0]+p[0])/2,(V[r][1]+p[1])/2)     #goto the mid point between random vertex and point

    if i % 1000 == 0:

        t = Turtle()
        t.up()
        t.hideturtle()
        window.update()

    print(i)



done()