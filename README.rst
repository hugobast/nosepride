Nosepride
~~~~~~~~~

|Build Status|

The colors are stolen from the minitest/pride plugin for minitest. This
plugin also formats traceback and error reports with less visual noise,
this was heavily inspired by rspec's report output.

Screenshot
~~~~~~~~~~

.. figure:: https://s3.amazonaws.com/hbastien/nosepride0.1.0.png
   :alt: Example console output

   Example console output
Installation
~~~~~~~~~~~~

::

    pip install nosepride

Usage
~~~~~

Nothing! Nosepride is on by default! But if you mush turn it off...

::

    nosetests --fabulous-off

Changelog
~~~~~~~~~

Version 0.1.5
^^^^^^^^^^^^^

Python 3.3 support!

Version 0.1.0
^^^^^^^^^^^^^

Plays better with other plugins (the tricky part is to avoid nosetests
regular output to leak out) Show docstring of test when one is available
Fixed bug in traceback printing (was filtering out relative file outputs
when we actually want those)

Version 0.0.6
^^^^^^^^^^^^^

Filtering out all path from traceback not directly on project path Empty
error message caused report to have nothing but a blank line, it now
prints the error class name

Version 0.0.4
^^^^^^^^^^^^^

Better failure formatting

License
~~~~~~~

The MIT License (MIT)

Copyright (c) 2014 Hugo Bastien

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

.. |Build Status| image:: https://travis-ci.org/hugobast/nosepride.png?branch=master
   :target: https://travis-ci.org/hugobast/nosepride