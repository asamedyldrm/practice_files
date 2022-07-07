# x = False
#
# if x:
#     print("Doğru.")
# else:
#     print("Yanlış.")
#
# print("Doğru") if x else print("Yanlış")
#
# sayi = 11
# if sayi % 2 == 0:
#     print("Çift")
# else:
#     print("Tek")
#
# print("Çift") if sayi % 2 == 0 else print("Tek")
#
# print("Çift" if sayi % 2 == 0 else "Tek")

a, b = 10, 5

# print("Her iki sayı eşittir" if a==b "a b'den büyüktür" elif a>b else "a b'den küçüktür")

print("her iki sayı eşittir" if a == b else "a b'den büyüktür" if a>b else "a b'den küçüktür" )
