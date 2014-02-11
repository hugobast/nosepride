from os.path import relpath, commonprefix
from mock import patch
from unittest import TestCase
from re import match
from nosepride.utils.traceback import Traceback

LINES = [
    'Traceback (most recent call last):\n',
    '  File "/home/username/project/nosepride/tests/test_nosepride.py"',
    ', line 12, in test_wraps_string_in_terminal_escaped_color_syntax\n',
    'raise Exception("Exception is raised")\n',
    'Exception: \x1b[31mException is raised\x1b[0m'
]
EXAMPLE_TRACEBACK = "".join(LINES)

FULL_TRACEBACK = """Traceback (most recent call last):
  File "/home/username/project/nosepride/tests/fields/fields.py", line 546, in test_datetime_validation
    self.assertRaises(ValidationError, log.validate)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/unittest/case.py", line 475, in assertRaises
    callableObj(*args, **kwargs)
  File "/home/username/project/nosepride/base/document.py", line 307, in validate
    field._validate(value)
  File "/home/username/project/nosepride/base/fields.py", line 174, in _validate
    self.validate(value, **kwargs)
  File "/home/username/project/nosepride/fields.py", line 373, in validate
    new_value = self.to_mongo(value)
  File "/home/username/project/nosepride/fields.py", line 393, in to_mongo
    return dateutil.parser.parse(value)
  File "/home/username/project/nosepride/python_dateutil-2.2-py2.7.egg/dateutil/parser.py", line 748, in parse
    return DEFAULTPARSER.parse(timestr, **kwargs)
  File "/home/username/project/nosepride/python_dateutil-2.2-py2.7.egg/dateutil/parser.py", line 310, in parse
    res, skipped_tokens = self._parse(timestr, **kwargs)
TypeError: 'NoneType' object is not iterable"""


class TestTraceback(TestCase):

    def test_nothing(self):
        Traceback(EXAMPLE_TRACEBACK)

    @patch("nosepride.utils.traceback.getcwd")
    def test_returns_a_formatted_line_for_file_reference(self, getcwd):
        getcwd.return_value = "/home/username/project/nosepride"
        traceback = Traceback(EXAMPLE_TRACEBACK)
        traceback.format_line()

        self.assertEqual(
            '# tests/test_nosepride.py:12:in '
            'test_wraps_string_in_terminal_escaped_color_syntax',
            traceback.formatted_lines[0]
        )

    @patch("nosepride.utils.traceback.getcwd")
    def test_return_a_full_report(self, getcwd):
        getcwd.return_value = "/home/username/project/nosepride"
        expected = [
            '# tests/fields/fields.py:546:in test_datetime_validation',
            '# /System/Library/Frameworks/Python.framework/Versions/2'
            '.7/lib/python2.7/unittest/case.py:475:in assertRaises',
            '# base/document.py:307:in validate',
            '# base/fields.py:174:in _validate',
            '# fields.py:373:in validate',
            '# fields.py:393:in to_mongo',
            '# python_dateutil-2.2-py2.7'
            '.egg/dateutil/parser.py:748:in parse',
            '# python_dateutil-2.2-py2.7.egg/dateutil/parser.py:310:in parse'
        ]

        traceback = Traceback(FULL_TRACEBACK)
        report = traceback.report()
        self.assertEqual(expected, report)

