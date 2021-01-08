# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 10:51:49 2020

@author: ADMIN
"""

import numpy as np

def gen_matrix(n):
    while True:
        A = np.random.randint(-5,5,(n,n))
        det = np.linalg.det(A)
        if det != 0:
            return A
            break


n = int(input('Nhập n:'))
print(gen_matrix(n))