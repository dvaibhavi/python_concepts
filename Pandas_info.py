import pandas as pd    

import numpy as np


dict_info = {'key1' : 2.0, 'key2' : 3.1, 'key3' : 2.2}  
series_obj = pd.Series(dict_info)    
print (series_obj)  

data_info = {'first' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),    
       'second' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}    
  
df = pd.DataFrame(data_info)    
#To add new column third
df['third']=pd.Series([10,20,30],index=['a','b','c'])    
print (df)    
#To add new column fourth
df['fourth']=df['first'] + df['third']    
print (df)  


df['3'] = pd.Series([5,6,7], index=['a', 'b', 'c'])

print(df)

df.drop(labels= ['3'],
axis=1,
inplace=True)

print(df)

df1 = pd.Series([2,10,8,9,-2, 6])

df2 = pd.Series([4,5,9,2,2])

#df1 = df1[~df1.isin(df2)]

df2 = df2[~df2.isin(df1)]

print("elements of df1 not in df2 are :- \n")
print(df2, "\n----------\n",  df1)

#del df.index.name
#print(df)


arr = np.array(([1,2,3,4],[1,2,3,4],[0,2,3,4],[1,2,3,4]), ndmin=6)

print(arr)