# print("1. Toplama")
# print("2. Çıkarma")
# print("3. Çarpma")
# print("4. Bölme")
# print("ç. Çıkış")
#
# choice = input("Seçiminiz: ")
# match choice:
#     case ("1"|"2"):
#         print("Toplama ve Çıkarma")
#     case "2":
#         print("Çıkarma")
#     case "3":
#         print("Çarpma")
#     case "4":
#         print("Bölme")
#     case "ç":
#         print("Çıkış")
#     case _: #case other şeklinde de olabilir.
#         print("Geçersiz seçim!")

# if choice == ("1"):
#     print("Toplama")
# elif choice == "2":
#     print("Çıkarma")
# elif choice == "3":
#     print("Çarpma")
# elif choice == "4":
#     print("Bölme")
# elif choice == "ç":
#     print("Çıkış")
# else:
#     print("Geçersiz")

# n = 0
# match n:
#     case n if n==0:
#         print("Sayı 0")
#     case n if n>0:
#         print("Sayı > 0")
#     case n if n<0:
#         print("Sayı < 0")

n = 1
match n:
    case 1:
        print("Sayı 1")
    case 2:
        print("Sayı 2")
    case 1:
        print("Sayı 1 ****")

        