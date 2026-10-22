import pandas as pd

a = pd.DataFrame({

    "City": ["Delhi","Mumbai","Delhi","Mumbai"],
    "Day": ["Monday","Tuesday","Monday","Tuesday"],
    "AQI": [180,90,220,110]
})

# Grouping = Suppose to find the average AQI of each city
z = a.groupby("City")["AQI"].mean()
print(z)

# agg() = lets you do multiple statistics in a group
w = a.groupby("City")["AQI"].agg(["mean","max","min"])
print(w)

# Grouping in two coloumns
f = a.groupby(["City","Day"])["AQI"].agg(["mean","max"])
print(f)

#-------------------------------------------------------------------------------------
# Sort values [Rearranging values in ascending or decending]
k = a.sort_values(by="AQI" , ascending=True)                 
print(k)                                            # ascending is false = Descending

# Sort values in multiple coloumns
x = a.sort_values(by=["AQI","City"], ascending=False)
print(x)

# Sort index
h = a.sort_index(ascending=False)
print(h)
#-------------------------------------------------------------------------------------

