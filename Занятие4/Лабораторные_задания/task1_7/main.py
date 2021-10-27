
list_ = [4, -1, 10, -10, 3, -3, -6, 8, 6, 90]
Sred = sum(list_)/len(list_)
print(Sred)
list_1 = []
for i in list_:
    i = i - Sred
    list_1.append(i)
print(list_1)