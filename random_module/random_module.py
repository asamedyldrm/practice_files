import random as r

# random fonksiyonu

# print(r.random())
# for i in range(5):
#     print(r.random())

# seed fonksiyonu

# r.seed(60)
# print(r.random()) #hep aynı sayıyı üretiyor.
# print(r.random())
# print(r.random())

# getstate ve setstate komutları

# r.seed(60)
#
# x = r.getstate()
# print(r.random())
#
# r.setstate(x)
# print(r.random())
#
# print(r.random())
# print(r.random())

# randint

# print(r.randint(100,250))

# randrange

# print(r.randrange(100))
# print(r.randrange(10, 250))
# print(r.randrange(10, 250, 5))

# getrandbits

# for i in range(10):
#     sayi = r.getrandbits(5) #maksimum 5 bit olacak şekilde sayı üretiyor.
#     print(sayi, bin(sayi))

# choice

numbers = [10, 20, 30, 40, 60, 80, 5, 9]
# print(r.choice(numbers))

# name = "PYTHON"
# print(r.choice(name))

# choices

# numbers = [10, 20, 30]

# print(r.choices(numbers, k=10))
# print(r.choices(numbers, k=10,
#                 weights=[98, 1, 1]))  # %98'i 1.sayıdan %1'i 2.sayıdan %1'i de 3.sayıdan seçer. 100 olmak zorunda değil!
# print(r.choices(numbers, k=10, cum_weights=[4, 6, 10]))  # kümülatif toplayarak gider. yani sırasıyla 4,6-4,10-4

# shuffle

numbers = [10, 20, 30, 40, 50, 60, 70]

# print(numbers)
r.shuffle(numbers)
# print(numbers) #tek satırlık emir olarak yazamayız. öncelikle karıştırıp sonra yazdırmak gerekiyor.

# sample fonksiyonu

# liste = ["Mavi", "Sarı", "Kırmızı"]
#
# print(r.choices(liste, k=2))  # bu iki seçtiği aynı olabilir. fakat sample 'da olmaz çünkü 2 adet örnek alıyor.
#
# print(r.sample(liste, 2))
# print(r.sample(liste, 4, counts= [2, 3, 3])) #3 mavi 2 sarı 3 kırmızıdan oluşan bir listeden sonuç alma işlemi.

# liste = range(1, 100)
# print(r.sample(liste, 5))

# Diğer rastgele sayı üretme Fonksiyonları

r.uniform(10, 20)
r.triangular(0, 100, 50)
r.variate... 
