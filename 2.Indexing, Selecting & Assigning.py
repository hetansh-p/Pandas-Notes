import pandas as pd

a = pd.DataFrame({
    "Year": [2017, 2018],
    "Apples": [35, None],
    "Bananas": [21, 34],
    "City": ["Delhi","Pune"]
})


# Indexing = .iloc[row,coloumn]

print(a.iloc[:,1])
print(a.iloc[1,:])
print(a.iloc[1,0])
print(a.iloc[-2,0])

# Label based selection = .loc[label of rows,label of coloumns]

print(a.loc[:,"Year"])
print(a.loc[:, "Apples"])

# Manuplating the index

a = a.set_index("Year")
print(a)

print(a.loc[2017])

# Conditional Selection
k = a["City"].isin(["Delhi","Pune"])
print(k)

z = a[a["Apples"].isnull()]
print(z)                              

s = a[(a["Bananas"]>20) & (a["Bananas"]<30)]          # (| = or)
print(s)                                              # (~ = not equal to)

# adding new data
a["Condition"] = ["Profit","Loss"]
print(a)