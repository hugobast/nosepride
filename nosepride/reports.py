from .utils.traceback import Traceback


class FailureReport(object):

    def __init__(self, formatter, result):
        result.printErrors = self.print_errors
        result.printSummary = self.print_summary

        self.formatter = formatter
        self.result = result

    def print_error_header(self, index, test):
        self.formatter.output("  {0}) {1}".format(
            unicode(index + 1),
            unicode(test)
        ))

    def print_blank_lines(self, count):
        [self.formatter.output("\n") for _ in range(count)]

    def print_traceback(self, error):
        traceback = Traceback(error).report()

        for line in self.formatter.get_next_failed_expectation().splitlines():
            self.formatter.output("     {0}\n".format(
                self.formatter.failure(line)
            ))

        for line in traceback:
            self.formatter.output("     {0}\n".format(
                self.formatter.stack(line)
            ))


    def print_errors(self):
        self.print_blank_lines(2)
        errors = self.result.errors + self.result.failures

        if not errors:
            return None

        self.formatter.output("Failures:")
        self.print_blank_lines(2)
        for index, (test, error) in enumerate(errors):
            self.print_error_header(index, test)
            self.print_blank_lines(2)
            self.print_traceback(error)
            self.print_blank_lines(1)

    def print_summary(self, start, stop):
        finale = "Ran %s fabulous tests in %.4f seconds" % (
            self.result.testsRun,
            stop - start
        )

        colored_finale = []
        for char in finale:
            colored_finale.append(self.formatter.pride(char))

        self.formatter.output("".join(colored_finale))
        self.print_blank_lines(2)