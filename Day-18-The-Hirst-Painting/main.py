#import colorgram

#kolorki = colorgram.extract("image.jpg", 31)
#kolorki.pop(0)

#rgb_colors = []

#for kolor in kolorki:
#    r = kolor.rgb.r/256
#    g = kolor.rgb.g/256
#    b = kolor.rgb.b/256
#    rgb_colors.append((r, g, b))
#    print(r, g, b)
#
#print(rgb_colors)


color_list = [(231, 233, 239), (238, 231, 234), (221, 232, 224), (208, 160, 82), (55, 89, 132), (145, 91, 40), (139, 26, 48), (222, 207, 105), (132, 176, 203), (45, 55, 104), (158, 46, 84), (170, 159, 40), (128, 189, 143), (84, 20, 44), (38, 43, 66), (187, 93, 106), (188, 138, 166), (84, 123, 182), (60, 39, 30), (79, 153, 165), (87, 157, 90), (195, 80, 71), (159, 201, 220), (79, 74, 43), (45, 74, 77), (59, 127, 116), (219, 175, 187), (167, 207, 166), (178, 188, 212), (146, 36, 33)]


import turtle as turtle_module
import random

turtle_module.colormode(255)
timmy = turtle_module.Turtle()
timmy.shape("circle")
timmy.pensize(20)
timmy.penup()
timmy.speed("fast")
timmy.setx(-250)
timmy.sety(-250)

for j in range(10):
    for i in range(10):
        temp_color = random.choice(color_list)
        timmy.color(temp_color)
        timmy.stamp()
        xcor = timmy.xcor()
        xcor += 50
        timmy.setx(xcor)
    timmy.setx(-250)
    ycor = timmy.ycor()
    ycor += 50
    timmy.sety(ycor)
timmy.hideturtle()

my_screen = turtle_module.Screen()
my_screen.exitonclick()
