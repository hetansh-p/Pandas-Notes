# Dataframe Representation

import pandas as pd

a = pd.DataFrame({   
    "Name" :["Jacob","William"], 
    "Age" :[9,10], 
    "Gender" :["Male","Male"]          
    })
print(a)

# Each Coloumn of a Dataframe is called Series
b = pd.Series([23,45,67],name = "NOGS" , index=["S-class","C-class","E-class"])
print(b)

# Operations in Series [Summary Functions]
print(b.max())
print(b.min())
print(b.shape)
print(b.describe())

# Reading Data files[CSV]

k = pd.read_csv("Any Dataset")




