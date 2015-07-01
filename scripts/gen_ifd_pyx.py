import os
import sys
fpath = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     '../fdint/ifd.pyx'))

with open(fpath, 'w') as f:
    f.write("""'''
Inverse Fermi-Dirac integrals.

This file was generated by `scripts/gen_ifd_pyx.py`, and should not
be edited directly.
'''
""")
    f.write('from fdint cimport _fdint\n')
    f.write('import numpy\n')
    for i in xrange(1,2,2):
        a = str(i).replace('-','m')
        f.write('''
def ifd{a}h(nu, out=None):
    cdef int num
    if isinstance(nu, numpy.ndarray):
        num = nu.shape[0]
        if out is None:
            out = numpy.empty(num)
        else:
            assert isinstance(out, numpy.ndarray) and out.shape[0] == num
        _fdint.vifd{a}h(nu, out)
        return out
    else:
        return _fdint.ifd{a}h(nu)
'''.format(a=a))
