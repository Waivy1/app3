import numpy as np
from PIL import Image
from random import randint


class Canvas:

    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
        self.color = (255, 255, 255)

        self.data = np.zeros((self.height, self.weight, 3), dtype=np.uint8)
        self.data[:] = self.color

    def make(self):
        img = Image.fromarray(self.data, 'RGB')
        img.save('canvas.png')


class Rectangle:

    def __init__(self, canvas):
        self.x = randint(1, canvas.height/2)
        self.y = randint(1, canvas.weight/2)
        self.height = randint(1, 20)
        self.weight = randint(1, 20)
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))

    def draw(self, canvas):
        canvas.data[self.x: self.x + self.height, self.y: self.y + self.weight] = self.color


canvas = Canvas(20, 20)

attempts = randint(1, 5)


for attempt in range(attempts):
    attempt = Rectangle(canvas)
    attempt.draw(canvas)

canvas.make()

