l = [1,2,3]
t = (1,2,3)
print(l)
print(t)

l[2] = 10
# t[2] = 10 #tuple verileri değiştirilemez yani immutable türdedir!
print(l)
print(t)

x,y,z = t
print(x)

z = 10
print(t)

t = (x,y,z) #ancak bu şekilde yeni bir tuple oluşturarak yapılabilir.
print(t)

v = ([1,2,3],[3,4,5])
print(v)
v[0][1] = 100
print(v)

t2 = 1,2,3
print(t2)