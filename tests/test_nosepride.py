from mock import Mock
from unittest import TestCase
from nosepride.nosepride import Nosepride
from nosepride.formatters.plain import Plain
from nosepride.formatters.fabulous import Fabulous
from nosepride.formatters.base import Base


class TestNosepride(TestCase):

    def test_wraps_string_in_terminal_escaped_color_syntax(self):
        color = Plain()
        self.assertEquals("\x1b[31m.\x1b[0m", color.pride("."))

    def test_raises_not_implemented_for_generate_colors_method(self):
        formatter = Base()
        with self.assertRaises(NotImplementedError):
            formatter.generate_colors()

    def test_cycles_through_primary_terminal_colors(self):
        Nosepride.formatter = Plain()
        plugin = Nosepride()
        self.assertEquals("\x1b[31m.\x1b[0m", plugin.pride("."))
        self.assertEquals("\x1b[32m.\x1b[0m", plugin.pride("."))
        self.assertEquals("\x1b[33m.\x1b[0m", plugin.pride("."))

    def test_cycles_through_fabulous_colors(self):
        Nosepride.formatter = Fabulous()
        plugin = Nosepride()
        self.assertEquals("\x1b[38;5;154m.\x1b[0m", plugin.pride("."))
        self.assertEquals("\x1b[38;5;154m.\x1b[0m", plugin.pride("."))
        self.assertEquals("\x1b[38;5;148m.\x1b[0m", plugin.pride("."))

    def test_raised_errors_without_message_gets_a_default_one(self):
        Nosepride.formatter = Fabulous()
        plugin = Nosepride()
        error = (ValueError, "", Mock(name="traceback"))
        plugin.record_error(Mock(name="Test"), error)

        self.assertIn("ValueError: ", plugin.failed_expectations)
