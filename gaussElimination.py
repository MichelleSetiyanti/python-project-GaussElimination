## Algoritma Gauss Elimination
## Step 1 : Mengubah soal yang dimuat menjadi sebuah matriks tringular
## x = gausElimin(a,b)- x dengan mengeliminasi Gaus

## Step 2 : install numpy
## numpy adalah library

import numpy as np 
## Ini adalah function
def gaussElimination(a,b):
    ## n = untuk menghitung length b
    n= len(b)
    #elimination phase
    for x in range(0,n-1):
        for i in range(x+1,n):
            if a[i,x] != 0.0:
                elim = a [i,x]/a[x,x]
                a[i,x+1:n] = a[i, x+1:n] - elim*a[x,x+1:n]
                b[i] = b[i] - elim*b[x]
    #back to subtitution
    for x in range (n-1,-1,-1):
        b[x] = (b[x] - np.dot(a[x,x+1:n],b[x+1:n]))/a[x,x]
    return b
