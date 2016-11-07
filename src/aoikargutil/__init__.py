# coding: utf-8
"""
Package.
"""
from __future__ import absolute_import

# Internal imports
import aoikargutil.aoikargutil as _aoikargutil


# Support usage like:
# `from aoikargutil import ensure_spec`
# instead of:
# `from aoikargutil.aoikargutil import ensure_spec`
#
# The use of `getattr` aims to bypass `pydocstyle`'s `__all__` check.
#
# For `aoikargutil.aoikargutil`'s each public attribute name
for key in getattr(_aoikargutil, '__all__'):
    # Store the attribute in this module
    globals()[key] = getattr(_aoikargutil, key)

# Delete the module reference
del _aoikargutil
