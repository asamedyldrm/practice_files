# class sirket:
#     zam_oran = 1.05
#     calisan_sayisi = 0
#
#     def __init__(self, ad, soyad, yas, maas):
#         self.ad = ad
#         self.soyad = soyad
#         self.yas = yas
#         self.maas = maas
#         sirket.calisan_sayisi += 1
#
#     def zam(self):
#         self.maas = self.maas * self.zam_oran
#
#     @classmethod
#     def genel_zam(cls,oran):
#         cls.zam_oran = oran
#
#
# samet = sirket("Samet", "YILDIRIM", 25, 5500)
# baki = sirket("Baki", "Kara", 45, 7000)
#
# samet.zam_oran = 1.5
# # baki.zam()
# print(baki.maas)
# print(samet.maas)
# print(samet.ad, samet.soyad, samet.yas)
# print(samet.zam_oran)
# print(baki.zam_oran)
# print(sirket.zam_oran)
# print(sirket.calisan_sayisi)
# sirket.genel_zam(2)
# samet.genel_zam(3) #classın genel zam oranını değiştirir.
# baki.zam()
# print(baki.maas)
# # Class Methodu
#
# samet_str = "Samet-Yıldırım-25-5000"
# baki_str = "Baki-Kara-45-8000"
#
# ad,soyad,yas,maas = samet_str.split("-")
# samet = sirket(ad,soyad,yas,maas)

# Alternative Constructor
# Class method ve Static metod

class sirket:
    zam_oran = 1.05
    calisan_sayisi = 0

    def __init__(self, ad, soyad, yas, maas):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.maas = maas
        sirket.calisan_sayisi += 1

    def zam(self):
        self.maas = self.maas * self.zam_oran

    @classmethod
    def genel_zam(cls,oran):
        cls.zam_oran = oran

    @classmethod
    def from_string(cls,emp_str):
        ad,soyad,yas,maas = emp_str.split("-")
        return cls(ad,soyad,int(yas),float(maas))

    @staticmethod
    def tatil(gun):
        if gun == "haftasonu":
            print("Bugün tatil.")
        else:
            print("Bugün tatil değil.")



kisi1_str = "Ali-Osman-30-6000"
kisi1 = sirket.from_string(kisi1_str)
print(kisi1.soyad)
sirket.tatil("haftasonu")