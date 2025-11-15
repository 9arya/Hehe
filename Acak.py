import secrets as sr 


s = int(input("masukan jumlah angka acak: "))
while True:
  acak = sr.choice([1,2,3,4,5,6,7,8,9,0])
  s -= 1
  print(acak)
  if s <= 0:
    print("beres")
    break 
  else:
    continue