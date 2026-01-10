import turtle
turtle.Screen().bgcolor("White")
turtle.Screen().setup(300,400)


pollygon = turtle.Turtle()
num_sides = 6
side_length =70
angle = 360 / num_sides
for i in range(num_sides):
    pollygon.forward(side_length)
    pollygon.right(angle)
turtle.done()