# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 14:58:28 2025

@author: Catalina
"""

import numpy as np
from ml_utils import mittag_leffler
import matplotlib.pyplot as plt

def fractional_zener_model(t, params):
    E0, E1, tau, alpha = params
    t = np.array(t)  # Assurer que t est un tableau NumPy
    z = - (t / tau) ** alpha
    ml_values = mittag_leffler(alpha, z)
    return E0 + E1 * ml_values

params = [6.5, 14, 4, 0.5]
t = np.linspace(0, 25, num=500)

fractional_zener_model(t, params)
plt.figure(figsize=(10, 5))
plt.plot(t, fractional_zener_model(t, params))
plt.xlabel("Time")
plt.ylabel("Zeiner")