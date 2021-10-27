list_1 = [10,34,50]
list_2 = []
N = sum(list_1)/len(list_1)
print(N)
for i in list_1:
    if i > N:
        list_2.append(i)
print(list_2)

