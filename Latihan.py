import random
print(" jawab soalnya dengan benar ini sangat sulit dan harus teliti\n kesempatanmu cuma 10 \n kalau jawabannya salah atau bukan angka atau ada spasi kesempatan dikurangi")
angka = random.choice(range (42, 8241))
soal = angka**2 
jawaban = angka 
kesempatan = 10
print(f" berapakah akar pangkat 2 dari {soal}")
while True:
  
  try:
    masukan = int(input("masukin jawabnnya: "))
    if masukan == jawaban:
      print("selamat kamu benar")
      break
    else:
      kesempatan -= 1 
      print(f"\nsalah, kesempatanmu sisa {kesempatan} hitung lagi akar pangkat 2 dari {soal}")
  except ValueError:
    kesempatan -= 1
    print(f"masukinya angka doang jangan ada huruf,simbol,spasi,atau apapun selain angka, kesempatan mu berkurang jadi {kesempatan}")
  if kesempatan == 0:
    print(f"yah kalah jawabannya yaitu {jawaban} \n latihan lagi ya")
    print("jangan sakit hati latihan lagi ya ")
    break
