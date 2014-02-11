from unittest import TestCase
from nosepride.formatters.plain import Plain
from nosepride.formatters.fabulous import Fabulous


class TestNosepride(TestCase):

    def test_nothing(self):
        self.assertFalse(Plain())

    def test_wraps_string_in_terminal_escaped_color_syntax(self):
        raise Exception("Exception is raised")
        color = Plain()
        self.assertEquals("\x1b[31m.\x1b[0m", color.pride("."))

    def test_cycles_through_primary_terminal_colors(self):
        color = Plain()
        self.assertEquals("\x1b[31m.\x1b[0m", color.pride("."))
        self.assertEquals("\x1b[32m.\x1b[0m", color.pride("."))
        self.assertEquals("\x1b[33m.\x1b[0m", color.pride("."))

    def test_cycles_through_fabulous_colors(self):
        color = Fabulous()
        self.assertEquals("\x1b[38;5;154m.\x1b[0m", color.pride("."))
        self.assertEquals("\x1b[38;5;154m.\x1b[0m", color.pride("."))
        self.assertEquals("\x1b[38;5;148m.\x1b[0m", color.pride("."))
