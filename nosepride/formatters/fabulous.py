from math import sin, pi
from itertools import cycle
from utils import lazy_property
from nosepride.formatters.plain import Plain

class Fabulous(Plain):

    def generate_colors(self):
        return map(self.calculate_color, range(0, 6 * 7 - 1))

    # colors calculation stolen from Minitest's Pride Plugin
    # https://github.com/seattlerb/minitest
    def calculate_color(self, n):
        n *= 1.0 / 6
        r = int(3 * sin(n) + 3)
        g = int(3 * sin(n + 2 * pi/3) + 3)
        b = int(3 * sin(n + 4 * pi/3) + 3)
        return 36 * r + 6 * g + b + 16

    def pride(self, string):
        return "{0}38;5;{1}m{2}{3}".format(
            self.escseq, self.colors.next(), string, self.endseq
        )

    @lazy_property
    def colors(self):
        return cycle(self.generate_colors())