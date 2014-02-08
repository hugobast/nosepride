from itertools import cycle
from nose.plugins import Plugin
from utils import lazy_property
from math import sin, pi

class Nosepride(Plugin):

    name = 'nosepride'
    enabled = False

    escseq = "\e["
    endseq = "\e[0m"

    def pride(self, string):
        return "{0}{1}m{2}{3}".format(
            self.escseq, self.colors.next(), string, self.endseq
        )

    @lazy_property
    def colors(self):
        return cycle(range(31, 37))


class Fabulous(Nosepride):

    def generate_colors(self):
        return map(self.calculate_color, range(0, 6 * 7 - 1))

    def calculate_color(self, n):
        n *= 1.0 / 6
        r = int(3 * sin(n) + 3)
        g = int(3 * sin(n + 2 * pi/3) + 3)
        b = int(3 * sin(n + 4 * pi/3) + 3)
        return 36 * r + 6 * g + b + 16

    @lazy_property
    def colors(self):
        return cycle(self.generate_colors())