x = {1,2,3}
x.add(4)
print(x)
y = {"a" ,"b","c"}
y.add("c") #c eklenmez
print(y)
k1= {1,2,3,4,5}
k1.discard(3)
print(k1)
k1 = {1,2,3,10,34,26,67}
k2 = {1,2,23,34,100}
print(k1.difference(k2))
print(k2.difference(k1))
print(k1.difference_update(k2)) #k1 güncellendi
print(k1)
k1 = {1,2,3,10,34,26,67}
k2 = {1,2,23,34,100}
print(k1.intersection(k2))
print(k1.intersection_update(k2)) #k1 güncellendi
print(k1)
k1 = {1,2,3,10,34,26,67}
k2 = {1,2,23,34,100}
print(k1.union(k2))
print("***********")
print(k1.update(k2))
print(k1)
