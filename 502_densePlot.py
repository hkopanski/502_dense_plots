# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 12:54:03 2022

@author: hkopansk
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.style as style
import seaborn as sns

mu = 0
sigma = 1

N = 1000

np.random.seed(1)

x1 = np.random.normal(mu, sigma, N)
x2 = np.random.normal(mu, sigma, N)

chi1 = np.random.chisquare(1, size = N)

z = []

for i in range(N):
    if x1[i] > x2[i]:
        z.append(x2[i])
    else:
        z.append(x1[i])
        
df_min = pd.DataFrame({"x1"   : x1,
                       "x2"   : x2,
                       "z"    : z,
                       "chi_1": chi1})

fig, axes = plt.subplots(2, 2, figsize = [10, 6], dpi = 175, tight_layout = True)
fig.suptitle('Density Plots')

#style.use("bmh")
#style.use("fivethirtyeight")
style.use("ggplot")

sns.kdeplot(ax = axes[1, 1], data = df_min, x = "x2", 
            fill = True, color = "blue")

sns.kdeplot(ax = axes[0, 1], data = df_min, x = "x1", 
            fill = True, color = "green")

sns.kdeplot(ax = axes[0, 0], data = df_min, x = "z", 
            fill = True, color = "orange")

sns.kdeplot(ax = axes[1, 0], data = df_min, x = map(lambda x: x**2, df_min["z"]), 
            fill = True, color = "black")

plt.show()