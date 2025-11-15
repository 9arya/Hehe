import pandas as pd 


a = {
  "nama":["arya","lukman","rafa","nendi"],
  "nomor":[1,2,3,4],
  "absensi":["izin","hadir","sakit","hadir"]
}
s = pd.DataFrame(a, index=range(1, len(a["nama"])+1))
print(s.loc[1])