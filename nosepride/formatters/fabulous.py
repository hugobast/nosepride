from math import sin, pi
from .base import Base


# colors calculation stolen from Minitest's Pride Plugin
# https://github.com/seattlerb/minitest

def calculate_color(iteration):
    iteration *= 1.0 / 6
    r = int(3 * sin(iteration) + 3)
    g = int(3 * sin(iteration + 2 * pi/3) + 3)
    b = int(3 * sin(iteration + 4 * pi/3) + 3)
    return 36 * r + 6 * g + b + 16


class Fabulous(Base):

    format = "{0}38;5;{1}m{2}{3}"

    def generate_colors(self):
        return map(calculate_color, range(0, 6 * 7 - 1))
