from turtle import *

tracer(0)
screensize(1000, 1000)
m = 10
lt(90)

for i in range(5):
    fd(30 * m)
    rt(90)
    fd(40 * m)
    rt(90)
up()
fd(20 * m)
rt(90)
fd(5 * m)
rt(90)
down()
for i in range(7):
    fd(10 * m)
    rt(90)
up()
for x in range(10, 50):
    for y in range(-5, 40):
        goto(x * m, y * m)
        dot(3, 'red')
update()
done()

# Ответ 30
