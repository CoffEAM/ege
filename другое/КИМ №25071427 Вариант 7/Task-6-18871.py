from turtle import *
lt(90)
screensize(1000, 1000)
m = 10
tracer(0)

for i in '12':
    fd(10*m)
    rt(90)
    fd(20*m)
    rt(90)
up()
bk(4*m)
rt(90)
fd(7*m)
lt(90)
down()
for i in '1234':
    fd(8*m)
    lt(90)
    fd(12*m)
    lt(90)
up()
fd(10*m)
down()
for i in '1234':
    fd(12*m)
    rt(90)
up()
for x in range(-10, 25):
    for y in range(-10, 25):
        goto(x*m, y*m)
        dot(3, 'red')
done()
