import turtle, random


tor= turtle.Turtle()
tor1= turtle.Turtle()
tor2= turtle.Turtle()

tor.pencolor("darkred")
tor1.pencolor("cyan")
tor2.pencolor("pink")

tor.speed(0)
turtle.delay(0)

for i in range(0,10000):
    tor.forward(random.randint(0,50))
    tor.left(20*random.randint(1,19))
    tor1.forward(random.randint(0,50))
    tor1.left(20*random.randint(1,19))
    tor2.forward(random.randint(0,50))
    tor2.left(20*random.randint(1,19))

input()