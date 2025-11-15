import pandas as pd

a = {"hari 1": 1, "hari 2": 1, "hari 3": 2}
b = pd.Series(a)
b.loc["hari 2"] += 3
print(b[b > 1])
