class Ogrenci:
    def __init__(self,ogrenciAdi,ogrenciSoyadi,ogrenciSinif):
        self.ogrenciAdi = ogrenciAdi
        self.ogrenciSoyadi = ogrenciSoyadi
        self.ogrenciSinif = ogrenciSinif
    def __str__(self):
        return f"{self.ogrenciSinif} sınıfından {self.ogrenciAdi} {self.ogrenciSoyadi} öğrencisi"

    class Soru:
        def __init__(self, dogruSayisi, yanlisSayisi):
            self.dogruSayisi = dogruSayisi
            self.yanlisSayisi = yanlisSayisi

        def netSayisi(self):
            return int(self.dogruSayisi - (self.yanlisSayisi % 4))

        def hesapla(self):
            return int(self.netSayisi() * 2);

        def __str__(self):
            return f"{self.hesapla()} puan"

ogrenci1 =Ogrenci("Mustafa","Kemal",15600)
print(ogrenci1)


