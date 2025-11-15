import pandas as pd 

s = pd.read_csv("amsa.csv")
f = s["Dimension"]
print(s.to_string())