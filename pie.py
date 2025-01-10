import math
import turtle
regulus = turtle.Turtle()
print(regulus)
def polygon(t, length):
    for i in range(3):
        t.fd(length)
        t.lt(360/3) #angle

def flower(t, n, r):
    for i in range(n):
        polygon(t, r)
        t.lt(360/n) 

flower(regulus, 5, 100)
turtle.mainloop()            


