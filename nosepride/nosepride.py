from itertools import cycle
from nose.plugins import Plugin
from utils import lazy_property


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