from random import randint


class Cube():
    def __init__(self, sides) -> None:
        self.sides = sides

    def random_side(self):
        value = randint(1, self.sides)
        print(value)


cube1 = Cube(5)
cube1.random_side()
