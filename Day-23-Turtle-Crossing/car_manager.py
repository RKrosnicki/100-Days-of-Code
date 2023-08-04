from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):

        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def add_a_car(self):
        y_randomizer = [random.randint(0, 240), random.randint(-240, 0)]
        temp_y = random.choice(y_randomizer)

        car = Turtle("square")
        car.penup()
        car.setheading(180)
        car.color(random.choice(COLORS))
        car.shapesize(1, 3)
        car.goto(300, temp_y)
        self.cars.append(car)

    def drive(self):
        for car in self.cars:
            car.forward(self.speed)

    def accelerate(self):
        self.speed += MOVE_INCREMENT

