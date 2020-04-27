#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 21:17:00 2020

@author: clark
"""


def sums_k_m_less_than_N(k,m,N):
    # sumsKMLessThanN
    big_sum = 0
    for L in range(1,N):
        if (L%k == 0) or (L%m == 0):
            big_sum += L
    return big_sum        
