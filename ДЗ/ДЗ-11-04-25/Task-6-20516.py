from turtle import *

screensize(1000,1000)
m = 30
lt(90)
tracer(0)

for i in '123':
    fd(2*m)
    rt(90)
    fd(3*m)
    lt(90)
rt(180)
fd(6*m)
rt(90)
fd(9*m)
up()
bk(3)
rt(90)
down()
for i in '12':
    fd(m)
    rt(90)
    fd(2*m)
    lt(90)
rt(180)
fd(3*m)
rt(90)
fd(4*m)
rt(90)
fd(m)
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*m, y*m)
        dot(3, 'red')
done()
update()
