from turtle import *

tracer(0)
screensize(1000, 1000)
m = 15
lt(90)

for i in '1234':
    fd(16*m)
    lt(90)
    fd(20*m)
    lt(90)
up()
fd(4*m)
lt(90)
fd(8*m)
rt(180)
down()
for i in '123':
    fd(35*m)
    lt(90)
    fd(6*m)
    lt(90)
up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x*m, y*m)
        dot(3, 'white')
update()
done()
