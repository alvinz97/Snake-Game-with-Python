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

        