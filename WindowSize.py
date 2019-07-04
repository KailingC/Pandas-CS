import numpy as np


#1
#Display of numpy arrays

import sys
np.set_printoptions(threshold=np.inf)


#2
#display of pandas dataframe
#all columns
pd.set_option('display.max_columns', None)
#all rows
pd.set_option('display.max_rows', None)
#original width 50
pd.set_option('max_colwidth',100)
