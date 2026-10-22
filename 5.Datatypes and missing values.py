import pandas as pd

a = pd.DataFrame({
    "City": ["Mumbai","Pune","Kolkata","Pune"],
    "AQI": [100,None,95,None],
    "Temp": [32.5,29.7,30.2,29.7]
})

# Datatype = A data type tells Python what kind of value a column contains
print(a.dtypes)

#-------------------------------------------------------------------------------------

# isnull() or isna().sum() is used to find no. of missing values 
print(a["AQI"].isnull().sum())

# notna = to identify values that are present
print(a.notna())

# ------------------------------------------------------------------------------------

# fillna() = to fill missing values 
a["AQI"] = a["AQI"].fillna(90)
print(a)

# dropna() = to remove missing values
print(a.dropna())

# astype() = type conversions of coloumns
a["Temp"] = a["Temp"].astype(int)
print(a)

#------------------------------------------------------------------------------------

# value_counts() = counting no. of objects in datasets
k = a["AQI"].value_counts()
print(k)

# unique() = gives the unique (non repeatig obj.) obj
# nunique() = no. of unique values
l = a["City"].unique()
print(l)

#------------------------------------------------------------------------------------

# drop_duplicates() = remove same rows
t = a.drop_duplicates()
print(t)
