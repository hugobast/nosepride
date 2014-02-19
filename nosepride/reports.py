from .utils.traceback import Traceback


class FailureReport(object):

    def __init__(self, formatter, result):
        result.printErrors = self.print_errors
        result.printSummary = self.print_summary

        self.formatter = formatter
        self.result = result

    def print_error_header(self, index, test):
        self.formatter.output("  {0}) {1}".format(
            unicode(index + 1), test.shortDescription() or unicode(test)
        ))

    def print_blank_lines(self, count):
        [self.formatter.output("\n") for _ in range(count)]

    def next_failure_message(self):
        return self.formatter.get_next_failed_expectation()

    def print_failure_message(self):
        for line in self.next_failure_message().splitlines():
            self.formatter.output("     {0}\n".format(
                self.formatter.failure(line)
            ))

    def print_traceback(self, error):
        for line in Traceback(error).report():
            self.formatter.output("     {0}\n".format(
                self.formatter.stack(line)
            ))

    def print_failure(self, error):
        self.print_failure_message()
        self.print_traceback(error)

    def print_error(self, error, index, test):
        self.print_error_header(index, test)
        self.print_blank_lines(2)
        self.print_failure(error)
        self.print_blank_lines(1)

    def callback_plugins_report(self):
        self.result.config.plugins.report(self.result.stream)

    def print_errors(self):
        self.print_blank_lines(2)
        errors = self.result.errors + self.result.failures

        if errors:
            self.formatter.output("Failures:")
            self.print_blank_lines(2)
            for index, (test, error) in enumerate(errors):
                self.print_error(error, index, test)

        self.callback_plugins_report()

    def print_colored_finale(self, finale):
        colored_finale = []
        for char in finale:
            colored_finale.append(self.formatter.pride(char))
        return colored_finale

    def print_summary(self, start, stop):
        finale = "Ran %s fabulous tests in %.4f seconds" % (
            self.result.testsRun, stop - start
        )

        colored_finale = self.print_colored_finale(finale)

        self.formatter.output("".join(colored_finale))
        self.print_blank_lines(2)
