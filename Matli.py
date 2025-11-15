from random import choice
from math import sqrt


poin = 0
while True:
  angka = choice(range(9, 101))
  soal = angka**2 
  jawaban = int(sqrt(soal))
  print(f"Berapakah akar pangkat 2 dari {soal}")
  try:
    masuk = int(input("masukan jawabannya: "))
    if masuk == jawaban:
      poin +=1
      print(f"selamat kamu benar\npoin kamu nambah 1 jadi: {poin}")
    else:
      poin -=1
      print(f"yang benar tuh {jawaban}\npoinmu ngurang 1 jadi{poin}")
  except ValueError:
    print("masukainnya angka doang jangan ada spasi,huruf,simbol,dan lainnya")
  if poin < -2:
    print("kamu kalah")
    break
  elif poin == 75:
    print("kamu menang")
    break
  else:
    continue