
# ini adalah program dari sistem pegas

import numpy as np
from gaussElimin import *

a= np.array([[ 5.0, -3.0, 2.0],
            [8.0, -5.0, 6.0],
            [ 3.0, 4.0, -3.0]])
b = np.array([3.0, 7.0, 15.0])

aOrig = a.copy()
bOrig = b.copy()
y= gaussElimin(a,b)
det = np.prod(np.diagonal(a))
print('y =\n',y)
print('\ndet =',det)
print('\nCheck: A*y =\n', np.dot(aOrig,y))
input("\nPress return to exit")
