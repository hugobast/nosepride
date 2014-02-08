from nose.plugins import Plugin

# Plugin interface methods

class PluginBase(Plugin):

    name = 'nosepride'
    enabled = False
    score = 100

    def options(self, parser, env):
        parser.add_option(
            "--fabulous",
            action="store_true",
            default=False,
            dest="fabulous",
            help="enable colour output"
        )

    def configure(self, options, conf):
        if options.fabulous:
            self.enabled = True

    def addFailure(self, test, err): pass
    def addError(self, test, err): pass
    def addSuccess(self, test): pass
    def addSkip(self, test=None, err=None): pass

    def setOutputStream(self, stream):
        self.stream = stream

    def output(self, string):
        self.stream.write(string)
