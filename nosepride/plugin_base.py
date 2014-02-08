from os import devnull
from nose.plugins import Plugin

# Plugin interface methods
# https://nose.readthedocs.org/en/latest/plugins/interface.html
class NullStream(object):

    def __init__(self, stream):
        self.stream = stream

    def __getattr__(self, name):
        return getattr(self.stream, name)

    def write(self, *args):
        return

    def writeln(self, *args):
        return self.stream.writeln(*args)


class PluginBase(Plugin):

    name = 'nosepride'
    enabled = True
    score = 199

    def options(self, parser, env):
        parser.add_option(
            "--fabulous",
            action="store_true",
            default=False,
            dest="fabulous",
            help="enable colour output"
        )

    def begin(self):
        self.running_test = False

    def beforeTest(self, test):
        self.running_test = True

    def afterTest(self, test):
        if self.running_test:
            self.addSkip()

    def configure(self, options, conf):
        if options.fabulous:
            self.enabled = True

    def prepareTestResult(self, result):
        result.stream = NullStream(result.stream)

    def setOutputStream(self, stream):
        self.stream = stream

    def addFailure(self, test, err):
        self.output(self.failure("f"))

    def addError(self, test, err):
        self.output(self.failure("e"))

    def addSuccess(self, test):
        self.output(self.pride("."))

    def addSkip(self, test=None, err=None):
        self.output(self.pride("*"))

    def output(self, string):
        self.stream.write(string)
        self.running_test = False
