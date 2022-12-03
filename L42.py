#Emily Rusch Kaylen Nyhuis
import turtle
sally = turtle.Turtle()
sally.color("yellow")

for side in range(4):
    if side == 1:
        sally.color("green")
    if side == 3:
        sally.color("orange")
    sally.forward(100)
    sally.right(90)
