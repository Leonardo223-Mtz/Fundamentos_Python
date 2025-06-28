import turtle as t
import math
x = -2 * (math.pi)
A = 100
b = 100
c = 0
d = 0
period = (2*(math.pi)/b)
y = A*(math.sin((period*x-c) + d))
t.penup()
t.goto(x,y)
t.pendown()
x = (-23*(math.pi)/12)
while x!=2*(math.pi):
    y = A*(math.sin((period*x-c) + d))
    t.goto(x,y)
    x = x + ((math.pi)/12)