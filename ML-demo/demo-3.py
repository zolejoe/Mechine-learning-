#画个正方形
'''
import turtle
turtle.pensize(10)  
turtle.pencolor("blue")
turtle.fd(100)
turtle.right(90)
turtle.fd(100)
turtle.right(90)
turtle.fd(100)
turtle.right(90)
turtle.fd(100)
'''

import turtle
def turtle_triangle():
    brad = turtle.Turtle()

    brad.shape("turtle")
    brad.color("blue")
    brad.speed(1)
    for _ in range(3):
        brad.right(60)
        brad.forward(200)
        brad.right(60)
 
    turtle.exitonclick()
turtle_triangle()

import turtle
def turtle_rectangle():
    brad = turtle.Turtle()

