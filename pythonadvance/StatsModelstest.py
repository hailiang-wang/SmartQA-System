#-*- coding:utf-8 -*-
from statsmodels.tsa.stattools import adfuller as ADF
import numpy as np

print ADF(np.random.rand(100))