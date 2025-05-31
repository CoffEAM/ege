from turtle import *

lt(90)
m = 10
screensize(1000, 1000)
tracer(0)

for i in '12':
    fd(6*m)
    rt(90)
    fd(12*m)
    rt(90)
up()
bk(3*m)
lt(90)
fd(5*m)
rt(90)
down()
for i in '1234':
    fd(6*m)
    rt(90)
up()
fd(8*m)
down()
for i in '1234':
    fd(8*m)
    rt(90)
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*m, y*m)
        dot(3, 'red')
update()
done()
