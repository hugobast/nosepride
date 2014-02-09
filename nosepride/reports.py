
class FailureReport(object):

    def __init__(self, formatter, result):
        result.printErrors = self.print_errors
        result.printSummary = self.print_summary

        self.formatter = formatter
        self.result = result

    def print_errors(self):
        self.formatter.output("\n\n")
        errors = self.result.errors + self.result.failures

        if not errors:
            return None

        self.formatter.output("Failures:\n\n")
        for index, (test, error) in enumerate(errors):
            self.formatter.output(unicode(index+1) + ") " + self.formatter.failure(unicode(test)))
            self.formatter.output("\n\n")
            self.formatter.output(self.formatter.stack(error))
            self.formatter.output("\n")

    def print_summary(self, start, stop):
        finale = "Ran %s fabulous tests in %.4f seconds" % (
            self.result.testsRun,
            stop - start
        )

        colored_finale = []
        for char in finale:
            colored_finale.append(self.formatter.pride(char))

        self.formatter.output("".join(colored_finale))
        self.formatter.output("\n\n")