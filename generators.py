# Bir listenin elemanlarının karesini almak istediğimizde:

def kare(s):
    res = []

    for i in s:
        res.append(i * i)
    return res


liste = [1, 2, 3]
print(kare(liste))


# aynı işlemi generator mantığı ile yapalım.
# generator'lar bütün cevaı hafıza tutmaz, biz sordukça değerleri döndürürler.
# generator'lar iterator'dır. next ile sonraki değerlerine erişebiliriz.

def kare_generator(s):
    for i in s:
        yield i * i


liste = [1, 2, 3]
k = kare_generator(liste)

print(next(k))
print(next(k))
print(next(k))


# print(next(k)) #exhaust oluyor. Tekrar baştan başlamak istiyorsak tekrar oluşturmak gerekiyor.

def kare_generator(s):
    for i in s:
        yield i * i


k = kare_generator(liste)

for res in k:
    print(res)

# print(next(k)) bittiği için hata veriyor.

# List Comprehension Oluşturur Gibi Generator Oluşturma

liste = [x * x for x in [1, 2, 3, 4, 5]]
print(liste)

g = (x * x for x in [1, 2, 3, 4, 5])
print(next(g))

print("--------")

for i in g:
    print(i)
# print(next(g))

g = (x * x for x in [1, 2, 3, 4, 5])
print(list(g))  # direkt olarak exhaust etmek için bu şekilde girebiliriz.


# GENERATORS

# Kısa yoldan iterator oluşturmaya olanak sağlar.
# Generator'lar istendiğinde elemanları döndürdükleri için hafızada tutmaz.
# list(generator) yaptığımızda bu özellik kaybolur.

# Generator Exercise

def range_gerenator(start, end, step):
    current = start

    while current < end:
        yield current
        print(current)
        current += step

r = range_gerenator(1,20,11)
print(next(r)) #sadece 1 değerini bastırıyor.
# generator'ı çalıştırdığımızda yield'i çalıştırır ve durur. Sonra kaldığı yerden devam eder.
print(next(r))

