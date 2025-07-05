import turtle as tt
from turtle import *

# Crear dos tortugas
t1 = tt.Turtle()
t2 = tt.Turtle()


t1.penup()
t1.setx(-100)
t1.pendown()

t2.penup()
t2.sety(-100)
t2.setx(-100)
t2.pendown()

for i in range(1,11):
    t1.penup()
    t1.forward(5)
    t1.pendown()
    t1.forward(25)

    t2.forward(i*7)
    t2.penup()
    t2.forward(5)
    t2.pendown()

done() 