# Python 3.10
# Pattern Match Estrutural

print(
"""\
Jogo da Tartaruga

Comandos:
    - move x y
    - move steps
    - turn angle (default 90)
    - draw shape size (line | circle)
    - write text
    - stop | exit
"""
)

from turtle import Turtle

turtle = Turtle()
turtle.shape("turtle")
turtle.speed(3)
turtle.color("Green", "Yellow")
turtle.penup()


while True:
    command = input("🐢>").strip().split()
    # move 2 3 - ["move", "2", "3"]
    if command[0] in ("exit", "stop"):
        break
    if command[0] == "draw":
        # draw line 40 - ["draw", "line", "40"]
        shape = command[1]
        size = float(command[2])
        turtle.pendown()
        if shape == "line":
            turtle.forward(size)
        elif shape == "circle":
            turtle.circle(size)
