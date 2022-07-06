l = [1, 2, 3]
m = [[1, 3, 5], [3,4,5], l]
print(m)

# l[1] = 100
# print(m)

mt = [[row[i] for row in m] for i in range(3)]

del(mt[1]) 
print(mt)