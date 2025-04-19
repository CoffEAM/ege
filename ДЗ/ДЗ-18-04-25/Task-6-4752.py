from turtle import *

lt(90)
screensize(1000, 1000)
m = 30
tracer(0)

for i in range(15):
    fd(4*m)
    rt(60)
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*m, y*m)
        dot(3, 'red')
goto(0, 0)
update()
done()
