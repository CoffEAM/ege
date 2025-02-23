from turtle import *

tracer(0)
screensize(1500, 1500)
lt(90)
m = 15

fd(25*m)
rt(45)
fd(50*m)
up()
bk(50*m)
rt(45)
fd(15*m)
lt(90)
fd(30*m)
down()
rt(180)
fd(60*m)
bk(5*m)
rt(90)
fd(31*m)
up()
for x in range(-20, 20):
    for y in range(-10, 60):
        goto(x*m, y*m)
        dot(3, 'red')
done()
