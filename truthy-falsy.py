# print("Truthy Değerler")
# print(bool(1))
# print(bool(1.0))
# print(bool(1+0j))
# print(bool("a"))
#
# print("Falsy Değerler")
# print(bool(0))
# print(bool(0.0))
# print(bool(0+0j))
# print(bool(""))
# print(bool(None))

a = "" #100 veya 1 veya 0 bunlar denenerek sonuçlar değiştirilebilir.
# 0'dan farklı ise veya boş değilse : True
if a: #aslında if bool(a):
    print("doğru")
else:
    print("yanlış")