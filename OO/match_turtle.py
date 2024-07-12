# Python 3.10
# Pattern Match Estrutural

from turtle import Turtle

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

turtle = Turtle()
turtle.shape("turtle")
turtle.speed(3)
turtle.color("Green", "Yellow")
turtle.penup()

while True:
    command: list[str] = input("🐢>").strip().split()
    # move 2 3 - ["move", "2", "3"]

    # switch - case  /  Estrutural
    match command:  # target do nosso match

        case ["move", *points]:
            match points:
                case [x, y]:
                    turtle.goto(float(x), float(y))
                case [steps]:
                    turtle.forward(float(steps))

        case ["turn", *options]:
            match options:
                case [angle]:
                    turtle.right(float(angle))
                case _:
                    turtle.right(90)

        case ["draw", shape, size]:
            turtle.pendown()
            match shape:
                case "circle":
                    turtle.circle(float(size))
                case "line":
                    turtle.forward(float(size))
            turtle.penup()

        case ["write", text]:
            turtle.write(" ".join(text), None, "center", "16pt 20")

        case ["exit" | "stop" | "quit"]:
            break

        case _:
            print("Invalid command")
