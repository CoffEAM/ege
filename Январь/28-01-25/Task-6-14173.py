from turtle import *

tracer(0)
screensize(1000, 1000)
lt(90)
m = 10
up()

for i in '12':
    down()
    for k in '12':
        fd(8*m)
        rt(90)
        fd(8*m)
        rt(90)
    up()
    fd(6*m)
    rt(90)
    fd(6*m)
    lt(90)
rt(180)
fd(4*m)

down()
for l in '1234':
    fd(8*m)
    rt(270)
up()
for x in range(-20,20):
    for y in range(-20, 20):
        goto(x*m, y*m)
        dot(3, 'red')
done()





