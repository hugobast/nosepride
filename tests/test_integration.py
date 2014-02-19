from os import path, unlink
from unittest import TestCase, TestSuite
from nose.plugins import PluginTester
from nose.plugins.xunit import Xunit
from nosepride import Nosepride


class TestIntegration(PluginTester, TestCase):
    activate = ""
    args = [
        '--with-xunit',
        '--xunit-file=xunit_test.xml'
    ]

    plugins = [Xunit(), Nosepride()]

    def tearDown(self):
        unlink(self.file)

    def test_plays_fair_with_other_plugins(self):
        self.file = path.abspath(path.join(
            path.dirname(__file__), '..', 'xunit_test.xml')
        )
        with open(self.file) as report:
            self.assertRegexpMatches(
                report.read(), r'<\?xml version="1.0" encoding="UTF-8"\?>'
            )

    def makeSuite(self):

        class InternalTests(TestCase):

            def runTest(self):
                self.assertTrue(True)

        return TestSuite([InternalTests()])