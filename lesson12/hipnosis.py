import turtle
turtle.Screen().bgcolor("lime")
turtle.Screen().title("Spiral")
pen =turtle.Turtle()
size =0
while True:
    for n in range(4):
        pen.fd(size+1)
        pen.left(90)
        size=size-5
    size=size+1