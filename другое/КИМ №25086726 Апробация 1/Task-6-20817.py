from turtle import *

lt(90)
m = 10
screensize(5000, 5000)
tracer(0)

for i in '123':
    fd(27*m)
    rt(90)
    fd(12*m)
    rt(90)
up()
fd(4*m)
rt(90)
fd(6*m)
lt(90)
down()
for i in '1234':
    fd(83*m)
    rt(90)
    fd(77*m)
    rt(90)
up()
for x in range(-10, 20):
    for y in range(-20, 40):
        goto(x*m, y*m)
        dot(3, 'red')
update()
done()
