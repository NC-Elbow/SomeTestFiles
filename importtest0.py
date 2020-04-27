#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 21:30:11 2020

@author: clark
"""

from projectEulerNo1 import *

class projectEuler:
    def __init__(self, k, m, N):
        self.k = k
        self.m = m
        self.N = N
        
    def no1_a(self):
        """
        we import sums_k_m_less_than_N from script projectEulerNo1.py
        """
        self.big_sum = sums_k_m_less_than_N(self.k, self.m, self.N)
        
    def no1_b(self):
        big_sum_1 = 0
        for L in range(1, self.N):
            #a = """ stuff """ 4
            if (L%self.k == 0) or (L%self.m == 0):
                big_sum_1 += L
        self.sum2 = big_sum_1        
        

