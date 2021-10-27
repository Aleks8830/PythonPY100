
list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
list_1 = []
for i in list_:
    if i > 0:
        i = i ** 3
    else:
        i = 0
    list_1.append(i)
print(list_1)


