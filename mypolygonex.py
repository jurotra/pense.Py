import turtle
import math
bob = turtle.Turtle()
alice = turtle.Turtle()
print(bob)
print(alice)
def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n) #angle

def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference/3) + 1
    length = circumference / n
    polygon(t, length, n)      


circle(bob, 100)
turtle.mainloop()
