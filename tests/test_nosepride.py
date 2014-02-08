from unittest import TestCase
from nosepride.nosepride import Nosepride, Fabulous


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

    def test_cycles_through_fabulous_colors(self):
        color = Fabulous()
        self.assertEquals("\e[154m.\e[0m", color.pride("."))
        self.assertEquals("\e[154m.\e[0m", color.pride("."))
        self.assertEquals("\e[148m.\e[0m", color.pride("."))