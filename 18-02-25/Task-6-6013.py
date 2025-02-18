from turtle import *

m = 35
screensize(1000, 1000)
lt(90)
tracer(0)

for i in '12':
    rt(120)
    fd(7*m)
rt(300)
for k in '12':
    rt(120)
    fd(7*m)
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*m, y*m)
        dot(3, 'red')
done()
