import pandas as pd

import numpy as np

data = pd.read_csv( '/Users/Vaibhavi_Deshpande/Documents/Python_concepts/data.csv')
class calculate:

    def __init__(self, data):
        self.stocks = stocks

    #aapl_data = self.data['AAPL']
    # min = sum(appl)/n

    def calculate_mean(self, stocks, column):
        """ returns mean of the csv column"""
        data = data[column]
        n = len(data)

        if n == 0:
            raise ValueError("No value present in AAPL array")
        
        if n == 1:
            return data[0]
        
        result = (sum(data) ) // n

        return result


    def calculate_std_deviation(self, data, column):
        """ returns standard deviation of the csv column"""
        mean = self.calculate_mean(data, column)
        square_sum = 0
        data = data[column]
        n = len(data)
        
        for i in range(n):
            
            square_sum += np.square(data[i]-mean)
        
        return np.sqrt(square_sum//n-1)

   

# typehint
    
print(calculate_mean(aapl_data))
print(calculate_std_deviation(aapl_data))   
    