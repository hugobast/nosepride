from nose.plugins import Plugin


def lazy_property(fn):
    attr_name = '_lazy_' + fn.__name__

    @property
    def __lazy_property__(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)
    return __lazy_property__


class PluginShim(Plugin):

    def beforeTest(self, test):
        self.before_test(test)

    def afterTest(self, test):
        self.after_test(test)

    def prepareTestResult(self, result):
        self.prepare_test_result(result)

    def setOutputStream(self, stream):
        self.set_output_stream(stream)

    def addFailure(self, test, err):
        self.add_failure(test, err)

    def addError(self, test, err):
        self.add_error(test, err)

    def addSuccess(self, test):
        self.add_success(test)

    def addSkip(self, test=None, err=None):
        self.add_skip(test, err)