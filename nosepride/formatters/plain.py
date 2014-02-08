from itertools import cycle
from utils import lazy_property
from nosepride.plugin_base import PluginBase

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

    @lazy_property
    def colors(self):
        return cycle(range(31, 37))