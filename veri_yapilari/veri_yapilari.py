liste = [1, 2, 3, 4]
print(liste)

liste.append(10)
print(liste)

liste.insert(2, 16)  # eklemek istediğimiz veriyi ilk parametre index sayısı olacak şekilde eklememize yarıyor.
print(liste)

liste.append(3)  # eklemek istediğimiz veriyi yazıyoruz.
print(liste)

liste.remove(3)  # çıkarmak istediğimiz veriyi yazıyoruz ve listeden siliyor.
print(liste)

print(liste.pop())  # yığındaki en son eklenen veriyi alır ve listeden çıkarır.
print(liste)  # listeden çıkarılmış hali.

print(liste.index(4))  # 4 sayısının listede kaçıncı sırada olduğunu bulmak için kullanılır.
isimler = ["Ali", "Mehmet", "Osman"]
print(isimler.index("Mehmet"))

print(isimler.count("Ali"))
isimler.append("Ali")
print(isimler.count("Ali"))

liste2 = [10, 2, 5, 3, 8, 26]

# liste.append(liste2) #append ile listenin içine ekler ve tek bir eleman olarak.
liste.extend((liste2)) #extend ile eklersek listenin içindeki tüm elemanları diğer listeye ekler.
print(liste)

liste.sort()
print(liste)

liste.clear()
# liste = []
print(liste)

liste3 = liste2 #hafıza tek bir liste var. O da liste2
print(liste3)
liste3.append(500) # hem liste2 ye hem de liste 3 e ekler bu yüzden.
print(liste3)
print(liste2)

liste4 = liste2.copy()
liste4.append(600)
print(liste4)
