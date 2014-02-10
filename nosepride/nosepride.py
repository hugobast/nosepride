from re import findall
from os import environ
from .formatters.fabulous import Fabulous
from .formatters.plain import Plain


Nosepride = Plain
if findall(r'^xterm|-256color$', environ.get("TERM")):
    Nosepride = Fabulous
