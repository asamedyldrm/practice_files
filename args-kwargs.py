# def toplama(a,b):
#     return a+b
#
# print(toplama(3,4))

# def toplama(*args):
#     toplam = 0
#     for i in args:
#         toplam += i
#     return toplam
# print(top4,5))

# def topla(*args):
#     print(type(args))
#
# topla(1,2,3,4,5)

# def topla(p, *args):
#     print(p)
#     print(args)
#
#
# topla(1, 2, 3, 4, 5)
#
#
# def topla(*args, p):
#     print(p)
#     print(args)


# topla(1, 2, 3, 4, p=5)  # burada p=5 ifadesi verirsek hata almayız.


# def yazdir(**kwargs):
#     print(kwargs)
#
#
# yazdir(ad="Ahmet", soyad="Yılmaz")

# def yazdir(**kwargs):
#     for k in kwargs:
#         print(k, kwargs[k])
#
# yazdir(ad="Ahmet", soyad="Yılmaz", yaş= 25)

def yazdir(*args, **kwargs):
    print(sum(args))
    for k in kwargs:
        print(k,":", kwargs[k])

yazdir(1,2,3,5, ad= "AHMET", soyad= "Yılmaz")
