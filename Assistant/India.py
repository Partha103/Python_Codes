import turtle

screen = turtle.Screen()
screen.title("Happy Independence Day")
screen.setup(width=800, height=600)
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(2)
t.width(2)

def draw_rectangle(color, width, height):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

def draw_indian_flag():
    t.penup()
    t.goto(-150, 150)
    t.pendown()
    draw_rectangle("orange", 300, 50)
    
    t.penup()
    t.goto(-150, 100)
    t.pendown()
    draw_rectangle("white", 300, 50)
    
    t.penup()
    t.goto(-150, 50)
    t.pendown()
    draw_rectangle("green", 300, 50)
    
    t.penup()
    t.goto(0, 50) 
    t.setheading(0)
    t.pendown()
    t.color("navy")
    t.circle(25)

    t.penup()
    t.goto(0, 75)
    t.setheading(0)
    t.pendown()

    for _ in range(24):
        t.forward(25)
        t.backward(25)
        t.left(15)  

def write_message():
    t.penup()
    t.goto(0, 200)
    t.color("blue")
    t.pendown()
    t.write("Happy Independence Day", align="center", font=("Arial", 24, "bold"))

def draw_flag_with_heading():
    write_message()
    draw_indian_flag()

draw_flag_with_heading()

turtle.done()