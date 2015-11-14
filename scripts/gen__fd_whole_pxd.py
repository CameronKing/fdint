# Copyright (c) 2015, Scott J Maddox. All rights reserved.
# Use of this source code is governed by the BSD-3-Clause
# license that can be found in the LICENSE file.
import os
import sys
fpath = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     '../fdint/_fd_whole.pxd'))

with open(fpath, 'w') as f:
    for i in xrange(0,21,2):
        a = str(i).replace('-','m')
        f.write('cdef double fd{a}h(double phi)\n'.format(a=a))