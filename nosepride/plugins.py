from utils import PluginShim
from streams import NullStream


# Plugin interface methods
# https://nose.readthedocs.org/en/latest/plugins/interface.html
class PluginBase(PluginShim):

    score = 199
    name = 'nosepride'
    stream = None
    enabled = True
    running_test = False

    def options(self, parser, env):
        parser.add_option(
            "--fabulous-off",
            action="store_false",
            default=True,
            dest="disabled",
            help="disable colour output"
        )

    def failure(self, string):
        raise NotImplementedError(
            "Please provide implementation for failure"
        )

    def pride(self, string):
        raise NotImplementedError(
            "Please provide implementation for pride"
        )

    def begin(self):
        self.running_test = False

    def before_test(self, test):
        self.running_test = True

    def after_test(self, test):
        if self.running_test:
            self.add_skip()

    def configure(self, options, conf):
        if not options.disabled:
            self.enabled = False

    @staticmethod
    def prepare_test_result(result):
        result.stream = NullStream(result.stream)

    def set_output_stream(self, stream):
        self.stream = stream

    def add_failure(self, test, err):
        self.output(self.failure("f"))

    def add_error(self, test, err):
        self.output(self.failure("e"))

    def add_success(self, test):
        self.output(self.pride("."))

    def add_skip(self, test=None, err=None):
        self.output(self.pride("*"))

    def output(self, string):
        self.stream.write(string)
        self.running_test = False
