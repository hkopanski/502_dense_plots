# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 13:49:15 2022

@author: hkopansk
"""

import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
import matplotlib.style as style
import seaborn as sns

np.random.seed(1)
random.seed(10)

mu = 0
sigma = 1
N = 1000
n = 100

x_i = np.random.normal(mu, sigma, N)
samples = random.sample(list(x_i), n)

error = np.random.normal(mu + 2, sigma, n)

df_sample = pd.DataFrame({"xi": samples,
                          "error" : error})

df_sample["yi"] = df_sample["xi"] + df_sample["error"]

fig, axes = plt.subplots(figsize = [10, 6], dpi = 175, tight_layout = True)

style.use("ggplot")

sns.kdeplot(data = df_sample, x = "yi", 
            fill = True, color = "blue")

sns.kdeplot(data = df_sample, x = "xi", 
            fill = True, color = "green")