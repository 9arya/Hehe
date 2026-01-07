print("Halo!,siapa namamu")
nama = input().strip()
if not nama:
  nama = "orang tak dikenal"

while True:
  hari = input(f"halo {nama} hari ini hari apa?").lower().strip()
  match hari :
   case "senin":
     print("sekarang upacara di sekolah")
     break
   case "selasa" :
     print("bosen yah masuk sekolah")
     break
   case "rabu":
    print("pertengahan minggu nih")
    break
   case "kamis" :
     print("asik sebentar lagi libur")
     break
   case "jumat":
     print("besok libur")
     break
   case "sabtu" | "minggu":
     print("wih libur nih")
     break
   case _ :
     print("itu bukan nama hari yang benar!")