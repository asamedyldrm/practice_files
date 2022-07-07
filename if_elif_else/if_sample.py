x = int(input("sayı giriniz: ")) #5
# tekler = []
# if x > 0:
#     for i in range(1, x+1):
#         if i%2 == 1:
#             tekler.append(i)
#     n = (tekler[len(tekler)-1]+1)/2
#     print(n**2)
# else:
#     print("Sıfırdan büyük sayı giriniz.")

if x>0:
    max_odd = x - 1 if x %2 ==0 else x
    print(f"1 ile {x} arasındaki tek sayıların toplamı {(((max_odd + 1 )/2)**2)}")
else:
    "Sıfırdan büyük bir sayı giriniz!"