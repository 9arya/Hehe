from random import randint


daftar=[]
for i in range(1,21):
  angka = randint(1,11)
  match angka :
    case 1:
      daftar.append(50)
    case 2:
      daftar.append(55)
    case 3:
      daftar.append(60)
    case 4:
      daftar.append(65)
    case 5:
      daftar.append(70)
    case 6:
      daftar.append(75)
    case 7:
      daftar.append(80)
    case 8:
      daftar.append(85)
    case 9:
      daftar.append(90)
    case 10:
      daftar.append(95)
    case 11:
      daftar.append(100)
print(f"ini daftar buatmu \n{daftar}")
for v in range(0,20) :
  print(f"{daftar[v]}")