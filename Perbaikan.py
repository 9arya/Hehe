import pandas as pd 
import numpy as np 

angka = np.arange(1, 41)
pangkat = angka**2 
tabel = {
  "Angka":angka ,
  "hasil pangkat 2": pangkat 
}
df = pd.DataFrame(tabel)
array = np.array(angka)
arr = np.array(pangkat)
print("kalau ini tabel")
print(df)
print("kalau ini angkanya: ")
print(array)
print("kalau ini hasil pangkatnya:")
print(arr)