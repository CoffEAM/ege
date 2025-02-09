from turtle import *

tracer(0)
screensize(1000,1000)
m = 20
lt(90)

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
bk(4*m)
rt(90)
down()
for k in '123':
    fd(m*1)
    rt(90)
    fd(2*m)
    lt(90)
rt(180)
fd(4*m)
rt(90)
fd(6*m)
rt(90)
fd(1*m)
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*m, y*m)
        dot(3, 'red')
done()

#16

