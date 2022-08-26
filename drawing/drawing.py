import turtle

roza = turtle.Turtle()
roza.color("blue", "yellow")
roza.pensize(3)
roza.begin_fill()


for i in range(17):
    roza.forward(100)
    roza.left(85)

roza.penup()
roza.forward(150)
roza.pendown()

for i in range(17):
    roza.forward(100)
    roza.left(85)


roza.end_fill()













turtle.done()