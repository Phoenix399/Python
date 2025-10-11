import turtle
turtle.Screen().setup(300,400)
turtle.Screen().bgcolor("blue")
pen = turtle.Turtle()
pen.color("yellow")
side = 100
sidelength = 100
angle = 360/side
for i in range(side):
    pen.forward(sidelength)
    pen.right(angle)
turtle.done()