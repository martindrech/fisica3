# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 09:24:16 2024

@author: Martin Drechsler
"""

from aux_funcs import plot_streamlines
import numpy as np
import matplotlib.pyplot as plt



N = 512
l = 5

plt.figure(1)
plt.clf()
fig, ax = plt.subplots(num =1)

q1, q2 = 1, -1

charges_positions = [
    [q1, 1, 0], 
    [q2, -1, 0]]

plot_streamlines(l, N, charges_positions, ax, fig, text = True, line_color = 'w',
                     lines = True, density = 1)

# ax.set_xlim(0, l)

plt.tight_layout()