from unittest import TestCase, SkipTest
from nosepride.nosepride import Plain, Fabulous


class TestNosepride(TestCase):

    def test_nothing(self):
        self.assertTrue(Plain())

    def test_wraps_string_in_terminal_escaped_color_syntax(self):
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

    def test_can_render_simple_failure(self):
        self.assertFalse(Plain())

    def test_can_render_simple_error(self):
        import bad_import
        self.assertTrue(Plain())

    def test_can_render_simple_skip(self):
        raise SkipTest("pending")
