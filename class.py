class Ucus():
    havayolu = "THY"

    def __init__(self, kod, kalkis, varis, sure, kapasite, yolcu):
        self.kod = kod
        self.kalkis = kalkis
        self.varis = varis
        self.sure = sure
        self.kapasite = kapasite
        self.yolcu = yolcu

    def __repr__(self):
        return "{} sefer sayılı ucus, sistemde oluşturulmuştur." .format((self.kod))
    def anons_yap(self):
        return "{} sefer sayili {}-{} ucusumuz {} dakika sürecektir.".format(self.kod,self.kalkis,self.varis,self.sure)
    def koltuk_sayisi_guncelle(self):
        return self.kapasite - self.yolcu
    def bilet_satis(self, bilet_adedi = 1):
        if self.yolcu + bilet_adedi <= self.kapasite:
            self.yolcu += bilet_adedi
            self.koltuk_sayisi_guncelle()
            return "{} adet bilet satılmıştır. Kalan koltuk sayısı: {}".format(bilet_adedi,self.koltuk_sayisi_guncelle())
        else:
            return "Uçak tamamen dolu!"
    def bilet_iptal(self, bilet_adedi = 1):
        if self.yolcu >= bilet_adedi:
            self.yolcu -= bilet_adedi
            return "{} adet bilet iptal edilmiştir, güncel koltuk sayisi {}." .format(bilet_adedi,self.koltuk_sayisi_guncelle())
        else:
            return "İşlem gerçekleştirilemedi. İptal edilecek kadar yolcu yok."
# ucus1 = Ucus() -böyle kalmayacak
ucus2 = Ucus("TK123", "IST", "ANK", 60, 300, 50)
print(ucus2.kod,ucus2.varis)

ucus3 = Ucus("TK223", "BOD", "ANK", 40, 250, 0)
print(ucus3.koltuk_sayisi_guncelle())
print(ucus3.bilet_satis(5))
print(ucus3.bilet_iptal(6))
print(ucus3.__dir__())
print(ucus3)
