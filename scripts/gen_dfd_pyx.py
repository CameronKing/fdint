# Copyright (c) 2015, Scott J Maddox. All rights reserved.
# Use of this source code is governed by the BSD-3-Clause
# license that can be found in the LICENSE file.
import os
import sys
fpath = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     '../fdint/dfd.pyx'))

with open(fpath, 'w') as f:
    f.write("""# Copyright (c) 2015, Scott J Maddox. All rights reserved.
# Use of this source code is governed by the BSD-3-Clause
# license that can be found in the LICENSE file.

# This file was generated by `scripts/gen_dfd_pyx.py`.
# Do not edit this file directly, or your changes will be lost.
'''
First derivatives of the Fermi-Dirac integrals.
'''
""")
    f.write('from fdint cimport _fdint\n')
    f.write('import numpy\n')
    for i in range(-9,22,2)+range(0,21,2):
        a = str(i+2).replace('-','m')
        f.write('''
def dfd{a}h(phi, out=None):
    cdef int num
    if isinstance(phi, numpy.ndarray):
        num = phi.shape[0]
        if out is None:
            out = numpy.empty(num)
        else:
            assert isinstance(out, numpy.ndarray) and out.shape[0] == num
        _fdint.vdfd{a}h(phi, out)
        return out
    else:
        return _fdint.dfd{a}h(phi)
'''.format(a=a))
