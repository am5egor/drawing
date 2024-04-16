from turtle import *

def sqr(x,y, colour):
    global i
    penup()
    goto(x,y)
    pendown()
    color('black', colour)
    begin_fill()
    for j in range(4):
        forward(30)
        left(90)
    end_fill()
    color('white')
    penup()
    goto(x + 10,y - 0)
    pendown()
    if i == 9:
        i = -1
    write(i+1, font=('Arial', 17, 'bold'))

colors = ['yellow', 'green', 'blue', 'red', 'pink', 'purple', 'skyblue', 'brown', 'orange', 'black']

x = -200
for i in range(10):
    sqr(x,200, colors[i])
    x += 40

penup()
goto(100,100)

    

def move(x,y):
    Dobbi.penup()
    Dobbi.goto(x,y)
    Dobbi.pendown()

def move_left():
    Dobbi.goto(Dobbi.xcor()-5, Dobbi.ycor())

def move_right():
    Dobbi.goto(Dobbi.xcor()+5, Dobbi.ycor())

def move_up():
    Dobbi.goto(Dobbi.xcor(), Dobbi.ycor()+5)

def move_down():
    Dobbi.goto(Dobbi.xcor(), Dobbi.ycor()-5)

def p_col1():
    Dobbi.color('yellow')

def p_col2():
    Dobbi.color('green')

def p_col3():
    Dobbi.color('blue')

def p_col4():
    Dobbi.color('red')

def p_col5():
    Dobbi.color('pink')

def p_col6():
    Dobbi.color('purple')

def p_col7():
    Dobbi.color('skyblue')

def p_col8():
    Dobbi.color('brown')

def p_col9():
    Dobbi.color('orange')

def p_col0():
    Dobbi.color('black')

def s_col1():
    scr.bgcolor('yellow')

def s_col2():
    scr.bgcolor('green')

def s_col3():
    scr.bgcolor('blue')

def s_col4():
    scr.bgcolor('red')

def s_col5():
    scr.bgcolor('pink')

def s_col6():
    scr.bgcolor('purple')

def s_col7():
    scr.bgcolor('skyblue')

def s_col8():
    scr.bgcolor('brown')

def s_col9():
    scr.bgcolor('orange')

def s_col0():
    scr.bgcolor('black')



Dobbi = Turtle()

Dobbi.shape('circle')
Dobbi.pensize(2)

scr = Dobbi.getscreen()
scr.listen()

scr.onscreenclick(move)
scr.onkey(move_left, 'Left')
scr.onkey(move_right, 'Right')
scr.onkey(move_up, 'Up')
scr.onkey(move_down, 'Down')

choise = 'pen'

scr.onkey(p_col1, '1')
scr.onkey(p_col2, '2')
scr.onkey(p_col3, '3')
scr.onkey(p_col4, '4')
scr.onkey(p_col5, '5')
scr.onkey(p_col6, '6')
scr.onkey(p_col7, '7')
scr.onkey(p_col8, '8')
scr.onkey(p_col9, '9')
scr.onkey(p_col0, '0')

def p_radius1():
    Dobbi.pensize(1)

def p_radius2():
    Dobbi.pensize(5)

def p_radius3():
    Dobbi.pensize(10)

def p_radius4():
    Dobbi.pensize(15)

def p_radius5():
    Dobbi.pensize(20)

scr.onkey(p_radius1, 'a')
scr.onkey(p_radius2, 's')
scr.onkey(p_radius3, 'd')
scr.onkey(p_radius4, 'f')
scr.onkey(p_radius5, 'g')

def begin_fill():
    Dobbi.begin_fill()

def end_fill():
    Dobbi.end_fill()

scr.onkey(begin_fill, 'z')
scr.onkey(end_fill, 'x')

def cleare():
    Dobbi.clear()

scr.onkey(cleare, 'c')


done()