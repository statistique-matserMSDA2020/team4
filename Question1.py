# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 21:47:15 2020

@author: MAMAN
"""

#Simulation loi binomiale et histogramme
import numpy as np
import scipy.stats as sps
import matplotlib.pyplot as plt
n, p, N= 30, 0.2, 10000
B= np.random.binomial(n, p, N)
f= sps.binom.pmf(np.arange(n+1), n, p)
plt.hist(B, bins=n+1, normed=1, range=(-0.5, n + 0.5), color = "grey")
plt.stem(np.arange(n+1), f, "r")
plt.title("Loi Binomiale")


#Simulation Loi Normale et densité
import numpy as np
import scipy.stats as sps
import matplotlib.pyplot as plt
mu, sigma, N = 3, 4, 10000
B= np.random.randn(N) * mu + sigma
x= np.linspace(-16, 16, 10000)
y= sps.norm.pdf(x, mu, sigma)
plt.plot(x, y, color="red")
plt.grid()
plt.title("Loi Normale")


#Simulation Loi Gamma et densité
import numpy as np
import scipy.stats as sps
import matplotlib.pyplot as plt
a, b, N = 10, 5, 10000
B= np.random.gamma(a, b, N)
x= np.linspace(-16, 20, 10000)
y= sps.gamma.pdf(x, a, b)
plt.plot(x, y, color="coral")
plt.grid()
plt.title("Loi Gamma")







