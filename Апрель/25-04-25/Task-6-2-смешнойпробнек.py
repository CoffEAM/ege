from turtle import *

screensize(15000, 15000)
tracer(0)
m = 30

rt(45)
for i in range(10):
    rt(45)
    fd(203*m)
    rt(45)
up()
bk(40*m)
rt(45)
down()
for i in '12345':
    fd(20*m)
    lt(90)
up()
for x in range(-250, -150):
    for y in range(-250, -150):
        goto(x*m, y*m)
        dot(3, 'red')
update()
done()
