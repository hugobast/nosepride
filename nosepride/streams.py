
class NullStream(object):

    def __init__(self, stream):
        self.stream = stream

    def __getattr__(self, name):
        return getattr(self.stream, name)

    def write(self, *args):
        return

    def writeln(self, *args):
        return self.stream.writeln(*args)