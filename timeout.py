#!/usr/bin/env python
#  vim:ts=4:sts=4:sw=4:et
#
#  Author: Hari Sekhon
#  Date: 2016-02-14 15:46:37 +0000 (Sun, 14 Feb 2016)
#
#  https://github.com/harisekhon/pytools
#
#  License: see accompanying Hari Sekhon LICENSE file
#
#  If you're using my code you're welcome to connect with me on LinkedIn and optionally send me feedback # pylint: disable=line-too-long
#
#  https://www.linkedin.com/in/harisekhon
#

"""

Tool to portably time out any command

"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
#from __future__ import unicode_literals

import os
import subprocess
import sys
libdir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'pylib'))
sys.path.append(libdir)
try:
    # pylint: disable=wrong-import-position
    from harisekhon import CLI
except ImportError as _:
    print('module import failed: %s' % _, file=sys.stderr)
    print("Did you remember to build the project by running 'make'?", file=sys.stderr)
    print("Alternatively perhaps you tried to copy this program out without it's adjacent libraries?", file=sys.stderr)
    sys.exit(4)

__author__ = 'Hari Sekhon'
__version__ = '0.1'


# Timeout behaviour itself is handled by my std base class CLI
class TimeoutCommand(CLI): # pylint: disable=too-few-public-methods

    def __init__(self):
        # Python 2.x
        super(TimeoutCommand, self).__init__()
        # Python 3.x
        # super().__init__()
        # special case to make all following args belong to the passed in command and not to this program
        self._CLI__parser.disable_interspersed_args()
        self._CLI__parser.set_usage('timeout [options] <your_command> <your_args> ...')

    def run(self):
        cmd = ' '.join(self.args)
        if not cmd:
            self.usage()

        sys.exit(subprocess.call(cmd, shell=True))


if __name__ == '__main__':
    TimeoutCommand().main()
