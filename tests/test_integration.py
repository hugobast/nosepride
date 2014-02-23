from os import path, unlink
from unittest import TestCase, TestSuite
from nose.plugins import PluginTester
from nose.plugins.cover import Coverage
from nose.plugins.xunit import Xunit
from nosepride.nosepride import Nosepride


class TestPluginIntegration(PluginTester, TestCase):
    activate = ""
    args = [
        '--with-xunit',
        '--xunit-file=xunit_test.xml',
        '--with-coverage',
        '--cover-package=nosepride'
    ]

    plugins = [Xunit(), Nosepride(), Coverage()]

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

        self.assertTrue("TOTAL" in self.output)

    def makeSuite(self):

        class InternalTests(TestCase):

            def runTest(self):
                self.assertTrue(True)

        return TestSuite([InternalTests()])


class TestShortDescription(PluginTester, TestCase):
    activate = ""
    plugins = [Nosepride()]

    def test_displays_test_docstring_when_present(self):
        self.assertTrue("Docstring" in self.output)

    def makeSuite(self):

        class InternalTests(TestCase):

            def runTest(self):
                """Docstring"""
                self.assertTrue(False)

        return TestSuite([InternalTests()])
