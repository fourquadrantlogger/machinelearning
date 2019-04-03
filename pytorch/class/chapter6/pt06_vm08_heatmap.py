# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 10:41:19 2018

@author: Administrator
"""

import numpy as np
from visdom import Visdom

vis = Visdom()

vis.histogram(X=np.random.rand(10000), opts=dict(numbins=20))
