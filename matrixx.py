# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 10:31:04 2021

@author: ADMIN
"""

import numpy as np

n = int(input('Nhập n:'))

def creat_matrix(n):
    while True:
        A = np.random.randint(-5,5,(n,n))
        det = np.linalg.det(A)
        if det != 0:
            print('Ma trận A:', A)
            return A
            break

def gen_matrix(A):
    det = np.linalg.det(A)
    print('Định thức của ma trận A:',det)
    return det

def rank(A):
    r = np.linalg.matrix_rank(A)
    print('Hạng của ma trận A:', r)
    return r

def muhai(A):
    exp = A @ A
    print('A^2 =',exp)
    return exp

def muba(A):
    exp3 = (A @ A) @ A
    print('A^3 = ',exp3)
    return exp3

def giaithua(k,A):
    if k == 1:
        return A
    else:
        return (A @ giaithua(k-1))

A = creat_matrix(n)
gen_matrix(A)
rank(A)
muhai(A)
muba(A)