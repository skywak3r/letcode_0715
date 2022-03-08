# -*- coding:utf-8 -*-

a = {}
a[1]=111
a[2]=222
b = {}
b[3]=111
b[2] = 2223
print(a.update(b))
for i,j in a.items():
    print(i,j)
# print(a.items())
# print(c)