from .utils.shims import PluginShim
from .streams import NullStream
from .reports import FailureReport


# Plugin interface methods
# https://nose.readthedocs.org/en/latest/plugins/interface.html
class PluginBase(PluginShim):

    score = 199
    name = 'nosepride'
    enabled = True

    def __init__(self):
        super(PluginBase, self).__init__()
        self.stream = None
        self.result = None
        self.failure_report = None
        self.expectation_iterator = None
        self.running_test = False
        self.failed_expectations = []

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

    def get_next_failed_expectation(self):
        if not self.expectation_iterator:
            self.expectation_iterator = iter(self.failed_expectations)
        try:
            return self.expectation_iterator.next()
        except StopIteration:
            return ""

    def record_error(self, test, err):
        self.failed_expectations.append("{0}: {1}".format(
            err[0].__name__, unicode(err[1])
        ))

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
        return result

    def set_output_stream(self, stream):
        self.stream = stream

    def add_failure(self, test, err):
        self.output(self.pride("!"))
        self.record_error(test, err)

    def add_error(self, test, err):
        self.output(self.pride("x"))
        self.record_error(test, err)

    def add_success(self, test):
        self.output(self.pride("."))

    def add_skip(self, test=None, err=None):
        self.output(self.pride("*"))

    def output(self, string):
        self.stream.write(string)
        self.running_test = False
