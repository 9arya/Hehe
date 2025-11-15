class burung:
  def __init__(self, warna = None ,jenis = None, ukuran = None, wilayah = None):
    self.warna = warna
    self.jenis = jenis
    self.ukuran = ukuran
    self.wilayah = wilayah
  def makan (self):
    print(f"burung {self.jenis} makan ")
  def mati(self):
    print("burung mati")
  def terbang(self):
    print(f"burung {self.jenis} terbang ke langit")
  def turun (self):
    print(f"burung {self.jenis} datang")

if __name__ == "__main__":
  manuk = burung("merah","kakak tua","10 cm","hutan ")
  
  manuk.turun()
  manuk.makan()
  manuk.terbang()