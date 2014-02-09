from unittest import TestCase
from nosepride.plugins import PluginBase


class TestPluginBase(TestCase):

    def test_nothing(self):
        self.assertTrue(PluginBase())

    def test_raises_not_implemented_for_failure_method(self):
        with self.assertRaises(NotImplementedError):
            PluginBase().failure("message")

    def test_raises_not_implemented_for_pride_method(self):
        with self.assertRaises(NotImplementedError):
            PluginBase().failure("message")