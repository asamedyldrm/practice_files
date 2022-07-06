# stack : yığın
# queue : sıra

l = [1, 2, 3]
l.append(50)
print(l)
print(l.pop())
print(l)
print(l.pop())
print(l)

l2 = [44, 55, 66]
l2.append(77)
print(l2.pop(0))
# print(l2.popleft())
print(l2)

from collections import deque

l3 = deque([11, 25, 60])
print(l3)
l3.append(70)
print(l3.popleft())
print(l3)
# print(l3.pop())
# print(l3)

