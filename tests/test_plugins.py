from unittest import TestCase

from mock import Mock

from nosepride.plugins import Nosepride
from nosepride.utils.lazy import lazy_property


class TestPluginBase(TestCase):

    @lazy_property
    def plugin(self):
        return Nosepride()

    def test_nothing(self):
        self.assertTrue(self.plugin)

    def test_sets_options_for_turning_nosepride_off(self):
        parser = Mock()
        self.plugin.options(parser, None)
        parser.add_option.assert_called_with(
            "--fabulous-off",
            action="store_false",
            default=True,
            dest="fabulous",
            help="disable colour output"
        )

    def test_begin_sets_running_test_to_false(self):
        self.plugin.begin()
        self.assertFalse(self.plugin.running_test)

    def test_before_test_sets_running_test_to_true(self):
        self.plugin.before_test(Mock(name="A test case"))
        self.assertTrue(self.plugin.running_test)

    def test_calling_after_test_with_running_test_true_calls_add_skip(self):
        self.plugin.running_test = True
        self.plugin.add_skip = Mock()
        self.plugin.after_test(Mock(name="A test case"))
        self.plugin.add_skip.assert_called_with()