import pandas as pd 

data = {
  "Nama":["gemini","claude"],
  "Batas":["seberesnya","dibatasi"],
  "model":["3.0","sonnet 4.5"],
  "dipakai":["sering","jarang"]
}
print(pd.DataFrame(data))