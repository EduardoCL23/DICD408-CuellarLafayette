# Required Libraries
import pandas as pd 
import numpy as np 

# Extraction
wine_url = "causa_de_muertes.csv"
wine_data = pd.read_csv(wine_url, header=None)


#Initial look at the data
print(wine_data.head())

# Loading
# Saving the transformed datas as a csv file
# wine_data.to_csv("wine_dataset.csv", index = False)
