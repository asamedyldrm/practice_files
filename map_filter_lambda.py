def karesini_al(x):
    return x ** 2


print(karesini_al(5))

# sayilar = [*range(1,6)]
# print(sayilar)
# for index in range(len(sayilar)):
#     sayilar[index] = karesini_al(sayilar[index])
# print(sayilar)

# map fonksiyonu
sayilar = [*range(1, 6)]
kareal = [*map(karesini_al, sayilar)]
print(kareal)

# filter fonksiyonu
def cift_sayilari_filtrele(x):
    return x if x % 2 == 0 else None
print(cift_sayilari_filtrele(10))

sayilar = [*range(1, 6)]
print([*filter(cift_sayilari_filtrele,sayilar)])

sayilar = [*range(1, 6)]
print([*map(lambda x: x*5,sayilar)])

sayilar = [*range(1, 10)]
print([*filter(lambda x:x if x%2==0 else None,sayilar)])