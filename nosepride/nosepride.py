from re import findall
from os import environ
from .plugins import PluginBase
from .formatters.plain import Plain
from .formatters.fabulous import Fabulous


formatter = Plain()
if findall(r'^xterm|-256color$', environ.get("TERM")):
    formatter = Fabulous()

PluginBase.formatter = formatter
Nosepride = PluginBase
