l = []

# for i in range(11):
#     l.append(i**2)
#     print(l)

# burada i'nin değer alması bi side effecttir. eğer bunu istemiyorsak lambda kullanabiliriz.

squares = list(map(lambda x: x ** 2, range(1, 11)))
print(squares)


def f(x):
    return x + 5


l2 = [2, 5, 8]

print(list(map(f, l2)))
print(list(map(lambda x: x + 5, l2)))

l3 = [z ** 2 for z in range(10)]
print(l3)

l4 = ([(x, y, z) for x in [1, 2, 3] for y, z in [(1, 2), (2, 3), (3, 4)] if True])
print(l4)

# (1,2,3,4)
# (2,3,4,5)
# (3,4,5,6)
# (4,5,6,7)

l5 = ([(a,b,c,d) for a,b,c,d in [(1,2,3,4),(2,3,4,5),(3,4,5,6),(4,5,6,7)]])
print(l5)
# print(list(map(lambda t:t+1, [1,2,3,4])))