import turtle

turtle.Screen().bgcolor("blue")
board = turtle.Turtle()
board.color("yellow")

#first triangle for the star
board.forward(100) #draw base

board.left(120) 
board.forward(100) #draw right side

board.left(120)
board.forward(100) #draw left side

board.penup()
board.right(150)
board.forward(100)

#second triangle for the star
board.pendown()
board.right(90)
board.forward(100) #draw base

board.right(120)
board.forward(100) #draw right side

board.right(120)
board.forward(100) #draw left side

turtle.done()

