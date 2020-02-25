from __future__ import print_function

import sys

if sys.hexversion < 0x02070000:
    print(70 * "*")
    print("ERROR: {0} requires python >= 2.7.x. ".format(sys.argv[0]))
    print("It appears that you are running python {0}".format(
        ".".join(str(x) for x in sys.version_info[0:3])))
    print(70 * "*")
    sys.exit(1)

import traceback
import os
import shutil
import jinja2

# import the helper utility module
from cesm_utils import cesmEnvLib
from diag_utils import diagUtilsLib

# import the plot baseclass module
from lnd_diags_plot_bc import LandDiagnosticPlot

class set_11(LandDiagnosticPlot):
    """Set 11 Plots
    """

    def __init__(self, env):
        super(set_11, self).__init__()

        # Set plot class description variables
        self._name = 'Set 11 Plots'
        self._shortname = 'set_11'
        self._template_file = 'set_11.tmpl'
        self.ncl_scripts = ['set_11.ncl']
        self.plot_env = env.copy()

    def check_prerequisites(self, env):
        # Set plot specific variables
        preq = 'No variables to set'
