import turtle
turtle.color("red")
a=15    #最小正方形的半径
turtle.penup()
turtle.goto(0,-120)   #初始位置
turtle.pendown()     
turtle.pensize(10)
turtle.speed(0)
# 从下往上，画中间的正方形，
for i in range(10):
    turtle.circle((i+1)*a,360,4)

turtle.penup()
turtle.goto(0,a*10*2-120)   #到达顶点
turtle.pendown()
# 从上往下，画中间的正方形形成交叉
for i in range(10):
    turtle.circle(-(i+1)*a,360,4)

# 画右上角的边缘部分
i=0
for j in range(4):
    turtle.setheading(-90*(i+1))
    turtle.circle(a,180,2)
    turtle.setheading(-90*i)
    turtle.circle(-a,-270,3)
    turtle.setheading(-90*i+45)
    turtle.circle((a**2*2)**0.5/2,180)
    turtle.setheading(-90*i)
    turtle.circle(-a,-180,2)
turtle.right(135)
turtle.circle(-(a**2*2)**0.5*2,270)
turtle.penup()
turtle.circle(-(a**2*2)**0.5*2,90)
turtle.pendown()
turtle.left(135)
turtle.circle(a,-90,1)
turtle.right(45)
turtle.circle(-(a**2*2)**0.5,270)

# 画右下角的边缘部分
i=1
for j in range(4):
    turtle.setheading(-90*(i+1))
    turtle.circle(a,180,2)
    turtle.setheading(-90*i)
    turtle.circle(-a,-270,3)
    turtle.setheading(-90*i+45)
    turtle.circle((a**2*2)**0.5/2,180)
    turtle.setheading(-90*i)
    turtle.circle(-a,-180,2)
turtle.circle(a,270,3)

#画左下角的边缘部分

i=2
for j in range(4):
    turtle.setheading(-90*(i+1))
    turtle.circle(a,180,2)
    turtle.setheading(-90*i)
    turtle.circle(-a,-270,3)
    turtle.setheading(-90*i+45)
    turtle.circle((a**2*2)**0.5/2,180)
    turtle.setheading(-90*i)
    turtle.circle(-a,-180,2)
turtle.right(135)
turtle.circle(-(a**2*2)**0.5*2,270)
turtle.penup()
turtle.circle(-(a**2*2)**0.5*2,90)
turtle.pendown()
turtle.left(135)
turtle.circle(a,-90,1)
turtle.right(45)
turtle.circle(-(a**2*2)**0.5,270)

#画左上角的边缘部分
i=3
for j in range(4):
    turtle.setheading(-90*(i+1))
    turtle.circle(a,180,2)
    turtle.setheading(-90*i)
    turtle.circle(-a,-270,3)
    turtle.setheading(-90*i+45)
    turtle.circle((a**2*2)**0.5/2,180)
    turtle.setheading(-90*i)
    turtle.circle(-a,-180,2)
turtle.circle(a,270,3)

#画最上方的吊绳及圆

turtle.right(90)
turtle.pensize(20)
turtle.forward(40)
turtle.pensize(10)
turtle.right(90)
turtle.circle(40)
turtle.left(90)
turtle.backward(40)

#画最下角的粗绳子
turtle.right(90)
turtle.circle(-a*10,180,2)
turtle.left(90)
turtle.pensize(50)
turtle.forward(40)

#画最下角的细绳子
turtle.pensize(2)
turtle.right(90)
turtle.forward(24)
turtle.left(90)
for i in range(13):
    turtle.forward(150)
    turtle.backward(150)
    turtle.left(90)
    turtle.penup()
    turtle.forward(4)
    turtle.pendown()
    turtle.right(90)

turtle.done()
