import numpy as np
import pandas as pd

df1 = pd.read_csv('Data/train.csv')
df2 = pd.read_csv('Data/test.csv')

print(df1.info())
print(df2.info())
