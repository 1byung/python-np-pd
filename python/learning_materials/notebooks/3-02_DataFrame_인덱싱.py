# DataFrame 인덱싱

import pandas as pd
import numpy as np

# Create sample DataFrame
data = {'names': ['Hyu','Hyu','Hyu','Charles','Charles'],
       'year':[2014,2015,2016,2015,2016],
       'points':[1.5,1.7,3.6,2.4,2.9]}
df = pd.DataFrame(data, columns=['year','names','points','penalty'],
                 index = ['one','two','three','four','five'])

df

# Get 'year' column only
df['year']
df.year

# Get multiple columns
df[['year','points']]

# Assign values
df['penalty'] = 0.5

df

# Assign different values per row
df['penalty'] = [0.1,0.2,0.3,0.4,0.5]

df

# Add column and assign values
df['zeros'] = np.arange(5)

df

val = pd.Series([-1.2, -1.5, -1.7], index = ['two','four','five'])

# Add 'debt' column with Series data (index alignment)
df['debt'] = val

df

df['net_points'] = df['points'] - df['penalty']

df['high_points'] = df['net_points'] > 2.0

df

# Delete existing columns
del df['high_points']
del df['net_points']
del df['zeros']

df

df.columns

df.index.name = 'Order'
df.columns.name = 'Info'
df

# Row control
df[0:3]

df['two':'four']

# .loc() - Search by row/column names

df.loc['two']

df.loc['two':'four']

# Get specific column values
df.loc['two':'four', 'points']

df.loc[:,'year']

# Get multiple columns
df.loc[:,['year','names']]

# Range indexing
df.loc['two':'four', ['year','names']]

# Add rows
df

df.loc['six', :] = [2017, 'Joohee', 3.3, 0.6, -1.3]
df

# .iloc() - Use numpy-style indexing (position-based)

df.iloc[3]

df.iloc[0:3, 0:2]

# Select rows and columns by position
df.iloc[[0,1,3], [1,2]]

df.iloc[:, 1:4]

# Get single value
df.iloc[1,1]

df.loc[:]

# Boolean indexing

# Find values in 'year' greater than 2014
df['year'] > 2014

add = df['year'] > 2014
df['add'] = add
df.loc[:]

df.loc[df['year'] > 2014, :]

df.loc[df['names'] == 'Hyunsuk', ['names', 'points']]

df.loc[(df['points'] > 2) & (df['points'] < 3), :]

# Assign new values conditionally
df.loc[df['points'] > 3, 'penalty'] = 0

df
