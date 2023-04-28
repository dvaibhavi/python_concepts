'''Write a NumPy program to create a 3x3 matrix with values ranging from 1 to 9.'''
import numpy as np

matrix = np.arange(1,10).reshape(3,3)
print(matrix)

print(np.zeros(10))
print(np.ones(10))
print(np.ones(10)*5)

import pandas as pd
data = {'sport': ['badminton', 'squash', 'football'],
        'players': ['a', 'b', 'c']}

df = pd.DataFrame(data)
print(df)

filtered_data = df[df['sport']=='a']
print(filtered_data, '\n', df[df['players']=='a'])


import plotly.express as px

x = np.array([1,2,3,4,5])
y = np.array([6,7,4,2,1])

fig = px.scatter(x=x, y=y)
fig.show()

x1 = np.array(['A', 'B', 'C', 'D'])
y1 = np.array([15, 0, 9, -2])

fig1 = px.bar(x=x1, y=y1)
fig1.show()

