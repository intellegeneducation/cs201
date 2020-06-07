# ColorSquareSpiral.py
import turtle   
t=turtle.Pen()
t.speed(0)
colors = ["red", "yellow", "blue", "green"]
for x in range(100):
    t.pencolor(colors[x % 4]) # mod / modulo
    t.forward(2 * x)        
    t.left(91)

