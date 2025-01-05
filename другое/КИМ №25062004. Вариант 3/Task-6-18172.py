from turtle import *
tracer(0)
lt(90)
screensize(1500, 1500)
m = 14

for i in range(9):
    fd(50*m)
    rt(90)
    fd(35*m)
    rt(90)
up()
fd(5*m)
rt(90)
fd(10*m)
rt(90)
down()
for i in range(4):
    fd(35*m)
    rt(90)
    fd(17*m)
    rt(90)
up()
for x in range(-15, 60):
    for y in range(-15, 60):
        goto(x*m, y*m)
        dot(3, 'red')

update()
done()

