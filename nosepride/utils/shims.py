from nose.plugins import Plugin

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