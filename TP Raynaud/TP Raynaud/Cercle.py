import turtle

cercle = turtle.Turtle()
cercle.speed(100)
turtle.delay(0)

for i in range(360):
    cercle.forward(1)
    cercle.right(1)

input()