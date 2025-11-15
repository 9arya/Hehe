import pandas as pd

df = pd.DataFrame({
    "nama": ["arya", "lukman", "rafa"],
    "kelas": ["8A","8I","8G"]
})

print(df["kelas"][2])
#kesalahnnya adlah pada bagian kelas tidak pakai []dimana ini diperlukan pada DataFrame dan juga pada bagian kelas hanya berisi 1 data sementara "nama" ada 3 jadi harus ditambah