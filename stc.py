# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 07:43:36 2021

@author: Sử Thành Công
"""
import numpy as np
import sympy as sp


def matran(m,n):
        #A = np.random.randint(-5,5,(m,n))
    A = np.random.randint(100, size=(m, n))
    return A


def rank_matran(A):
    rank = np.linalg.matrix_rank(A)
    return rank


def bac_thang(A):
    A = sp.Matrix(A).rref()[0]
    return np.array(A)


m = int(input('Nhập m:'))
n = int(input('Nhập n:'))

a = matran(m,n)
r = rank_matran(a)
b = bac_thang(a)

print("Matrix :\n {} ".format(a))
print('Hạng của ma trận:',r)
print('Chuyển thành ma trận bậc thang:\n',b)