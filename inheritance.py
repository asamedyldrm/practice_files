class Sirket:
    zam_oran = 1.1
    calisan_sayisi = 0

    def __init__(self, ad, soyad, yas, maas):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.maas = maas
        Sirket.calisan_sayisi += 1

    def zam(self):
        self.maas = self.maas * self.zam_oran

class IT(Sirket):
    zam_oran = 1.4
    def __init__(self,ad,soyad,yas,maas,dil,deneyim):
        super().__init__(ad,soyad,yas,maas)
        self.dil = dil
        self.deneyim = deneyim
    def deneyim_yazdir(self):
        return f"Bu kisinin {self.deneyim} yıl deneyimi var."

kisi_1 = Sirket("Mehmet", "Yılmaz", 21, 6000)
kisi_2 = Sirket("Ece", "Ak", 25, 8000)
it_1 = IT("Ahmet", "Yılmaz", 25, 5000,"Python", 10)

print(it_1.deneyim_yazdir())
print(it_1.dil)
print(it_1.zam_oran)
it_1.zam()
print(it_1.maas)
print(kisi_2.zam_oran)

print(isinstance(IT,Sirket))
print(isinstance(it_1,Sirket))
print(issubclass(IT,Sirket))
print(issubclass(Sirket,IT))


# Burada IT classının super class'ı Sirket classı oluyor.
# Inherit ettiğimiz class'a parent/super class, inherit edilene de child/sub class deniliyor.
# IT classının hiç bir şey yazmasak da Sirket'e erişimi var.
# Yani subclass'ın superclass'ının hem attributelarına hem de metodlarına ERİŞİMİ VAR!