class Sirket:
    zam_oran = 1.1
    calisan_sayisi = 0

    def __init__(self, ad, soyad, yas, maas): #init bir magic methoddur.
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.maas = maas
        Sirket.calisan_sayisi += 1

    def zam(self):
        self.maas = self.maas * self.zam_oran

    def __str__(self): #objenin okunabilir bir tanımını oluştururuz.
        return f"{self.ad} {self.soyad} isimli çalışan {self.yas} yaşındadır ve {self.maas} TL maaş almaktadır."

    def __add__(self, other):
        return self.maas + other.maas

    def __len__(self):
        return len(self.ad)

kisi1 = Sirket("Ahmet", "Ak", 25, 5000)
kisi2 = Sirket("Ayse", "Kara", 30, 6000)

print(kisi1+kisi2)
print(kisi1)
print(len(kisi1))