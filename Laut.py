import numpy as np 
import pandas as pd 
print("ini tabelnya silahkan dilihat")
t = {
  "Angka Asli":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
  "Angka Pangkat":[1,4,9,16,25,36,49,64,81,100,121,144,169,196,225]
}
print(pd.DataFrame(t, index=(list(range(1, len(t["Angka Asli"])+1)))))
print("kalau ini daftar angka pangkat 2 nya")
q = np.array(
  [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
  )

print(q**2)
