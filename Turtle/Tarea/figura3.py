import turtle as tt
from turtle import *
import math


tt.left(90)
tt.forward(200)
tt.right(90)
tt.forward(200)
tt.left(135)
rads = math.radians(45)
c = 200 * math.sin(rads)
tt.forward(c)
tt.left(90)
tt.forward(c)
tt.left(90)
diagonal = (200**2 + 200**2)**0.5
tt.forward(diagonal)
tt.left(135)
tt.forward(200)
tt.left(135)
tt.forward(diagonal)
tt.left(135)
tt.forward(200)
done()