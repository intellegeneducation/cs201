#PrintSquareFunction.py
import turtle
t = turtle.Pen()

# define function - print square 
def print_square(length, degree): # length = 100
    #length = 100
    t.forward(length)
    t.left(degree)
    t.forward(length)
    t.left(degree)
    t.forward(length)
    t.left(degree)
    t.forward(length)
    t.left(degree)

# calling function
print_square(100, 90) # draw square with length = 100
t.forward(100)
print_square(200, 100) # draw square with length = 200