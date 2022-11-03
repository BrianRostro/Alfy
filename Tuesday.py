import turtle

xrostro = turtle.Turtle()
xrostro.shape("turtle")
xrostro.resizemode("auto")

def right():
    xrostro.seth(0)
    xrostro.fd(100)

def left():
    xrostro.seth(180)
    xrostro.fd(100)

def up():
    xrostro.seth(90)
    xrostro.fd(100)

def down():
    xrostro.seth(270)
    xrostro.fd(100)

def draw_eyes():
    xrostro.pu()
    xrostro.setpos(-25, 35) 
    xrostro.pd()
    xrostro.circle(10)
    xrostro.pu()
    xrostro.setpos(45, 35)
    xrostro.pd()
    xrostro.circle(10)

def draw_nose(edge=10):
    xrostro.pu()
    xrostro.setpos(0, 10)
    xrostro.pd()
    xrostro.setpos(10, -10)
    xrostro.setpos(-10, -10)
    xrostro.setpos(0, 10)

def draw_leftear():
    xrostro.pu()
    xrostro.setpos(-40, 60)
    xrostro.pd()
    xrostro.circle(10)
    xrostro.pu()
    xrostro.setpos(-30, 70)
    xrostro.pd()
    xrostro.circle(20)

def draw_rightear():
    xrostro.pu()
    xrostro.setpos(60, 60)
    xrostro.pd()
    xrostro.circle(10)
    xrostro.pu()
    xrostro.setpos(70, 70)
    xrostro.pd()
    xrostro.circle(20)

def draw_smile():
    xrostro.pu()
    xrostro.setpos(-20, -20)
    xrostro.pd()
    turtle.circle(20, 180)


def rectangle():
    xrostro.pu()
    xrostro.setpos(-50, 50)
    xrostro.pd()
    right()
    down()
    left()
    up()
    draw_eyes()
    draw_nose()
    draw_leftear()
    draw_rightear()
    draw_smile()

    turtle.done()    

rectangle()


# -35, 35 and 35, 35 are the location for the circle eyes on the left and right side.