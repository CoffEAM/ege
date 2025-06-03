from turtle import *

lt(90)
m = 10
screensize(1000, 1000)
tracer(0)

for i in '12':
    fd(23*m)
    lt(90)
    bk(27*m)
    lt(90)
up()
bk(5*m)
rt(90)
fd(11*m)
lt(90)
down()
for i in '12':
    fd(26*m)
    rt(90)
    fd(32*m)
    rt(90)
up()
for x in range(-10, 40):
    for y in range(-10, 40):
        goto(x*m, y*m)
        dot(3, 'red')
update()
done()
