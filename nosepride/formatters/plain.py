from itertools import cycle
from ..utils.lazy import lazy_property
from ..plugins import PluginBase


class Plain(PluginBase):

    escseq = "\x1b["
    endseq = "\x1b[0m"

    def pride(self, string):
        return "{0}{1}m{2}{3}".format(
            self.escseq, self.colors.next(), string, self.endseq
        )

    def failure(self, string):
        return "{0}31m{1}{2}".format(
            self.escseq, string, self.endseq
        )

    def stack(self, string):
        return "{0}36m{1}{2}".format(
            self.escseq, string, self.endseq
        )

    def generate_colors(self):
        return range(31, 37)

    @lazy_property
    def colors(self):
        return cycle(self.generate_colors())