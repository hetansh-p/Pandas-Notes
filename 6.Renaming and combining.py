import pandas as pd

day1 = pd.DataFrame({
    "City": ["Delhi","Pune"],
    "AQI": [180,90]
}, index=["Delhi","Maharashtra"])

day2 = pd.DataFrame({
    "City": ["Mumbai","Delhi"],
    "AQI": [120,200]
})



#            |------> axis = 1 for combining coloumns side by side
#            |
# concat() = combining two datasets  ,[ignore_index=True] gives rows a new index from 0-3
combined = pd.concat([day1,day2],ignore_index=True)
print(combined)
#-------------------------------------------------------------------------------------
# join() = combines two datasets through common index name
# eg..   combined = aqi.join(temperature)

# merge() = Combines two DataFrames by matching values in a common column
# eg..   combined = pd.merge(aqi_data,temperature_data,on="City")
#-------------------------------------------------------------------------------------

# a.rename(coloumns{"old name" : "new name"})
# a.rename_axis("new name") = give the index a new name
b = day1.rename_axis("India")
print(b)