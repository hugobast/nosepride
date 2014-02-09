from utils import PluginShim
from streams import NullStream
from reports import FailureReport


# Plugin interface methods
# https://nose.readthedocs.org/en/latest/plugins/interface.html
class PluginBase(PluginShim):

    score = 199
    name = 'nosepride'
    stream = None
    result = None
    enabled = True
    running_test = False
    failure_report = None

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

    def stack(self, string):
        raise NotImplementedError(
            "Please provide implementation for pride"
        )

    def formatError(self, test, err):
        return err[0], self.failure(err[1]), err[2]

    def formatFailure(self, test, err):
        return err[0], self.failure(err[1]), err[2]

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

    def prepare_test_result(self, result):
        result.stream = NullStream(result.stream)
        self.failure_report = FailureReport(self, result)

    def set_output_stream(self, stream):
        self.stream = stream

    def add_failure(self, test, err):
        self.output(self.pride("!"))

    def add_error(self, test, err):
        self.output(self.pride("x"))

    def add_success(self, test):
        self.output(self.pride("."))

    def add_skip(self, test=None, err=None):
        self.output(self.pride("*"))

    def output(self, string):
        self.stream.write(string)
        self.running_test = False
