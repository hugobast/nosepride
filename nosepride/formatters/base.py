from itertools import cycle
from ..utils.lazy import lazy_property


class Base(object):

    escseq = "\x1b["
    endseq = "\x1b[0m"
    format = "{0}{1}{2}{3}"

    def generate_colors(self):
        raise NotImplementedError(
            """
            Please provide

            def generate_colors(self, string):
                # ... list of colors
            """
        )

    def pride(self, string):
        return self.format.format(
            self.escseq, next(self.colors), string, self.endseq
        )

    @lazy_property
    def colors(self):
        return cycle(self.generate_colors())

    def failure(self, string):
        return "{0}31m{1}{2}".format(
            self.escseq, string, self.endseq
        )

    def stack(self, string):
        return "{0}36m{1}{2}".format(
            self.escseq, string, self.endseq
        )
