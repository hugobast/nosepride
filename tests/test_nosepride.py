from unittest import TestCase
from nosepride.nosepride import Nosepride


class TestNosepride(TestCase):

    def test_nothing(self):
        self.assertTrue(Nosepride())

    def test_wraps_string_in_terminal_escaped_color_syntax(self):
        color = Nosepride()
        self.assertEquals("\e[31m.\e[0m", color.pride("."))

    def test_cycles_through_primary_terminal_colors(self):
        color = Nosepride()
        self.assertEquals("\e[31m.\e[0m", color.pride("."))
        self.assertEquals("\e[32m.\e[0m", color.pride("."))
        self.assertEquals("\e[33m.\e[0m", color.pride("."))
        self.assertEquals("\e[34m.\e[0m", color.pride("."))
        self.assertEquals("\e[35m.\e[0m", color.pride("."))
        self.assertEquals("\e[36m.\e[0m", color.pride("."))