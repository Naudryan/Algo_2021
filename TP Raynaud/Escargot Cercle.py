import turtle

escargotcercle = turtle.Turtle()
x=1
escargotcercle.speed(0)
turtle.delay(0)

while 1==1:
    escargotcercle.forward(1)
    escargotcercle.left(1000/(1*x))
    x += 1