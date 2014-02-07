from itertools import cycle
from nose.plugins import Plugin
from utils import lazy_property


class Nosepride(Plugin):
    name = 'nosepride'
    enabled = False

    def pride(self, string):
        return "\e[{0}m{1}\e[0m".format(
            self.colors.next(), string
        )

    @lazy_property
    def colors(self):
        return cycle(range(31, 37))