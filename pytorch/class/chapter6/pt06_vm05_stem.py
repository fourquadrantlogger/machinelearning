# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 10:39:29 2018

@author: Administrator
"""

import math

import numpy as np
from visdom import Visdom

vis = Visdom()

# stemplot
Y = np.linspace(0, 2 * math.pi, 70)
X = np.column_stack((np.sin(Y), np.cos(Y)))
vis.stem(
    X=X,
    Y=Y,
    opts=dict(legend=['Sine', 'Cosine'])
)
