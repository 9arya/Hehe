import base91

while True:
  print("pilih:\n1.encode\n2.decode\n3.keluar")
  try:
    pilihan = int(input(">>").strip())
    if pilihan == 1:
      pesan = input("apa pesannya:").encode("UTF-8")
      print(base91.encode(pesan))
    elif pilihan == 2:
      kode = input("apa kodenya:").encode("UTF-8")
      hasil = base91.decode(kode)
      print(hasil.decode("UTF-8"))
    elif pilihan == 3:
      break 
    else:
      print("pilihanmu tidak valid")
  except ValueError:
    print("masukan tidak valid")