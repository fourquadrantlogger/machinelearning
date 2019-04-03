# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 10:42:41 2018

@author: Administrator
"""

import numpy as np
from visdom import Visdom

vis = Visdom()

# boxplot
X = np.random.rand(100, 2)
X[:, 1] += 2

vis.boxplot(
    X=X,
    opts=dict(legend=['Men', 'Women'])
)
