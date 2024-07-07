from turtle import *
import colorsys

import colorsys

#bgcolor('green')
speed(0.3)
h=0.8
penup()
lt(90)
fd(100)
rt(90)
pendown()

for i in range(63):
    c=colorsys.hsv_to_rgb(h,1,1)
    fillcolor(c)
    begin_fill()
    h+=0.005
    circle(60-i,90)
    lt(80)
    circle(60-i,90)
    rt(60)
    end_fill()

    for j in range(2):
        lt(100)

rt(90)
penup()
fd(70)
pendown()
fd(160)
lt(180)

def leaf():
    color('green')
    begin_fill()
    circle(30,100)
    lt(90)
    circle(35,80)
    end_fill()
    color('black')
    lt(140)
    fd(10)
    lt(45)
    fd(10)
    lt(180)
    fd(10)
    lt(120)
    fd(5)
    rt(45)
    fd(10)
    lt(180)
    fd(10)
    rt(120)
    fd(5)
    lt(45)
    fd(11)
    lt(180)
    fd(10)
    lt(120)
    fd(5)
    rt(45)
    fd(9)
    lt(180)
    fd(10)
    rt(120)
    fd(5)
    lt(45)
    fd(8)
    lt(180)
    fd(8)
    lt(130)
    #hideturtle()
    fd(13)
    lt(183)
    fd(43)

speed(0)
color('green')
pensize(2)
circle(100,40)
leaf()
lt(130)
fd(20)
rt(90)
leaf()
rt(160)
leaf()
lt(150)
fd(25)
rt(50)
leaf()
lt(3)
fd(55)
lt(90)
leaf()
penup()
lt(90)
fd(50)
pendown()
lt(45)
leaf()
leaf()

rt(130)
circle(20,90)
rt(60)
leaf()
fd(10)
lt(80)
leaf()

fd(20)
rt(33)
color('green')
circle(35,80)
rt(170)
fd(50)
rt(80)
fd(3)
leaf()
fd(5)
rt(140)
fd(35)
rt(5)
leaf()
fd(3)
lt(35)
leaf()
fd(3)
lt(50)
fd(110)
lt(90)

def pot():
    fd(45)
    rt(110)
    fd(45)
    rt(70)
    fd(60)
    rt(70)
    fd(45)
    rt(110)
    fd(45)
color('brown')
begin_fill()
pot()
end_fill()

color('green')
pensize(2)
lt(90)
fd(166)
lt(180)
fd(166)
rt(90)
fd(2)
rt(90)
rt(3)
fd(40)
hideturtle()
done()