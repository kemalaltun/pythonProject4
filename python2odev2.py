class Insan:
    yetenekler =[""]
    def __init__(self,ad,soyad,yas,ulke,sehir,*yetenekler):
        self.ad=ad
        self.soyad=soyad
        self.yas=yas
        self.ulke=ulke
        self.sehir=sehir
        arr=[]
        for x in yetenekler:
            arr.append(x)
        self.yetenekler=arr
    def kisiBilgileri(self):
        return f"isim:{self.ad}\nsoyisim:{self.soyad}\nyaş:{self.yas}\nülke:{self.ulke}\nşehir:{self.sehir}\nyetenekler:{self.yetenekler}"
    def yetenekEkle(self,*yetenek):
        arr =[]
        for x in self.yetenekler:
            arr.append(x)
        for x in yetenek:
            arr.append(x)
        self.yetenekler = arr



insan1=Insan("Kemal","Altun","23","Türkiye","Ankara","Python")
print(insan1.kisiBilgileri())
insan1.yetenekEkle("CSS")
print(insan1.kisiBilgileri())