#program yang dibuat karena tantangan chatgpt
import pandas as pd #memasukan paket pandas as untuk menyingkat tidak harus pd namun umumnya pakai pd

layar_data = pd.read_csv("Exam_Score_Prediction.csv")#berfungsi membaca file Exam_Score_Prediction.csv
#print(layar_data.to_string())#ditambahkan to_string agar python menampilkan semua data
layar_data.info()
print(layar_data.head(15))
print("===="*20)
print(layar_data.describe())