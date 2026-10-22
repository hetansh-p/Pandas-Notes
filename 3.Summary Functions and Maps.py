# Mapping Data

import pandas as pd

data = pd.DataFrame({
    "City": ["Delhi", "Mumbai", "Pune"],
    "AQI": [80, 120, 160]
})

# To subtract 2 from every aqi value
a = data["AQI"].map(lambda x : x-2)
print(a)

# To replae values
b = data["City"].map({

    "Delhi":"North",
    "Pune":"West"
})
print(b)