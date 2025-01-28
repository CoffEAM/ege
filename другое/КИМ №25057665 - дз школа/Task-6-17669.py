from turtle import *

tracer(0)
screensize(1000, 1000)
m = 10
lt(90)

for i in '1234':
    fd(19*m)
    rt(90)
    fd(30*m)
    rt(90)
up()
fd(2*m)
rt(90)
fd(8*m)
lt(90)
down()
for k in '1234':
    fd(93*m)
    rt(90)
    fd(97*m)
    rt(90)
up()
for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x*m, y*m)
        dot(3, 'red')

done()




