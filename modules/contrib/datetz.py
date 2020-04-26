# pylint: disable=C0111,R0903

"""Displays the current date and time.

Parameters:
    * date.format: strftime()-compatible formatting string
    * date.locale: locale to use rather than the system default
"""

import core.decorators
from .datetimetz import Module

class Module(Module):
    @core.decorators.every(hours=1)
    def __init__(self, config):
        super().__init__(config)

    def default_format(self):
        return '%x %Z'

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4