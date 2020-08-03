import pygame
import sys
import random
import time

class Snake():
    def __init__(self):
        self.position = [100, 50]
        self.body = [[100, 50], [90, 50], [80,50]]
        self.direction = "RIGHT"
        self.changeDirectionTo = self.direction

    def changeDirTo(self, dir):
        if dir == "RIGHT" and not self.direction == "LEFT":
            self.direction = "RIGHT"

        if dir == "LEFT" and not self.direction == "RIGHT":
            self.direction = "LEFT"

        if dir == "UP" and not self.direction == "DOWN":
            self.direction = "UP"

        if dir == "DOWN" and not self.direction == "UP":
            self.direction = "DOWN"

    def move(self, foodPosition):
        if self.direction == "RIGHT":
            self.position[0] += 10

        if self.direction == "LEFT":
            self.position[0] -= 10

        if self.direction == "UP":
            self.position[0] += 10

        if self.direction == "DOWN":
            self.position[0] -= 10

        self.body.insert(0, self.position)

        if self.position == foodPosition:
            return 1
        else:
            self.body.pop()
            return 0

        def chackCollision(self):
            if self.position[0] > 490 or self.position[0] < 0:
                return 1

            elif self.position[1] > 490 or self.position[1] < 0:
                return 1

            for bodyPart in self.body[1:]:
                if self.position == bodyPart:
                    return 1
                return 0

        def getHeadPosition(self):
            return self.position

        def getBody(self):
            return self.position


class FoodSpawer():
    def __init__(self):
        self.position = [random.randrange(1,50) * 10 , random.randrange(1,50) * 10 ]
        self.isFoodOnScreen = True

    def spawerFood(self):
        if self.isFoodOnScreen == False:
            self.position = [random.randrange(1,50) * 10 , random.randrange(1,50) * 10 ]
            self.isFoodOnScreen = True
        return self.position

        