# -*- coding: utf-8 -*-
"""
Created on Fri May  1 23:25:10 2020

@author: MAMAN
"""

import numpy.random
import random
import math
import numpy
def integration(fonction,a,b,N):
    fonction, a, b, N = 1-x^2, 0, 1, 10000
    x = a+(b-a)*numpy.random.random_sample(N)
    p = 1.0/(b-a)
    f = fonction(x)
    moyenne = f.sum()/(N*p)
    g = f*f
    variance = g.sum()*1.0/(N*p*p)-moyenne*moyenne
    return (moyenne,math.sqrt(variance/N)*1.96)
