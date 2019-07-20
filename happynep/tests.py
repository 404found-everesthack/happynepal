import inline as inline
import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from IPython import get_ipython
ipy = get_ipython()
if ipy is not None:
    ipy.run_line_magic('matplotlib', 'inline')
train = pd.read_csv('titanic/titanic_train.csv')
test = pd.read_csv('titanic/titanic_test.csv')

