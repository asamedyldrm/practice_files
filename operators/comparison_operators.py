import math

a = 5.0
b = 4.99998
print(math.isclose(a, b, abs_tol=0.0001))
print(math.isclose(a, b, rel_tol=1e-5))

# import decimal
# a = decimal.Decimal("1.25")
# b = decimal.Decimal("1.25")

# a = "A"
# b = "Z"
# print(a==b)
# print(a<b)
# print(a>b)
# print(a<=b)
# print(a>=b)
# print(a!=b)

# a = 2.675 - 1
# print(a)
# print(round(a, 3) == 1.675)

# a = 5.0
# b = 4.99998
# print(abs(a-b)<0.0001) #bu şekilde tolerans değeri vererek eşit olup olmadıklarını kontrol edebiliriz.
