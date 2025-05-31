from turtle import *

lt(90)
screensize(1000, 1000)
tracer(0)
m = 25

rt(30)
for i in '123':
    rt(150)
    fd(6*m)
    rt(30)
    fd(12*m)
up()
for x in range(-20, 10):
    for y in range(-20, 10):
        goto(x*m, y*m)
        dot(3, 'red')
update()
done()

#30
