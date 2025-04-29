from turtle import *

m = 10
screensize(2000, 2000)
tracer(0)

for i in '12':
    fd(5*m)
    rt(90)
    fd(11*m)
    rt(90)
up()
fd(-4*m)
rt(90)
fd(6*m)
lt(90)
down()
for i in '12':
    fd(42*m)
    rt(90)
    fd(63*m)
    rt(90)
up()
for x in range(0, 60):
    for y in range(-60, 10):
        goto(x*m, y*m)
        dot(3, 'red')
update()
done()
