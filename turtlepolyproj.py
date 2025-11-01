import turtle

# setup
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# function to draw and fill any polygon
def draw_polygon(sides, length, color):
    angle = 360 / sides
    t.color(color)
    t.begin_fill()
    for _ in range(sides):
        t.forward(length)
        t.left(angle)
    t.end_fill()

# draw equilateral triangle
t.penup()
t.goto(-200, 100)
t.pendown()
draw_polygon(3, 100, "cyan")

# draw rectangle
t.penup()
t.goto(0, 100)
t.pendown()
t.color("lime")
t.begin_fill()
for _ in range(2):
    t.forward(150)
    t.left(90)
    t.forward(80)
    t.left(90)
t.end_fill()

# draw hexagon
t.penup()
t.goto(200, 100)
t.pendown()
draw_polygon(6, 70, "magenta")

# swirl animation effect (like your style)
t.penup()
t.goto(0, -100)
t.pendown()
for x in range(360):
    t.pencolor(colors[x % 6])
    t.width(x / 100 + 1)
    t.forward(x / 3)
    t.left(59)

turtle.done()
