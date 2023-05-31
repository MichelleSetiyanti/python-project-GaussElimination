
# ini adalah program dari sistem pegas

import numpy as np
from gaussElimination import *
import math
##ini adalah soal 
a= np.array([[ 2.0, 5.0, 3.0],
            [3.0, 4.0, 2.0],
            [ 1.0, 3.0, 1.0]])
b = np.array([1.0, -3.0, 2.0])

##y adalah hasil akhir
y= gaussElimination(a,b)

## ini adalah rumus untuk mencari determinan
det = np.prod(np.diagonal(a))

## ini adalah validasi matriks singular 
if math.isnan(det):
    det="Matriks Singular karena determinannya 0"
    print('y = 0\n',)
else:
    det = np.prod(np.diagonal(a))
    print('y =\n',y)

  
print('\ndet =',det)
