from turtle import *

lt(90)
screensize(1000, 1000)
m = 10
tracer(0)

for i in '12':
    fd(28*m)
    rt(90)
    fd(18*m)
    rt(90)
up()
fd(14*m)
rt(90)
fd(10*m)
lt(90)
down()
for i in '12':
    fd(30*m)
    rt(90)
    fd(7*m)
    rt(90)
up()
for x in range(-10, 30):
    for y in range(-10, 30):
        goto(x*m, y*m)
        dot(3, 'red')
update()
done()
