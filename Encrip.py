from base64 import a85decode
from base64 import a85encode
import binascii

while True:
  print("ketik 1 buat dekripsi 2 buat enkripsi")
  try:
   pilihan = int(input("ketik disini :").strip())
   if pilihan == 1:
     try:
      pesan = input("masukan pesanmu:")
      print(a85decode(pesan))
     except binascii.Error:
       print("yang kamu ketik bukan hasil enkripsi yang sesuai")
   elif pilihan == 2:
     pesan = input("masukan pesanmu:").encode("UTF-8")
     print(a85encode(pesan))
   else:
     print("pilihanmu tak ada dalam daftar")
  except ValueError:
    print("error nih")