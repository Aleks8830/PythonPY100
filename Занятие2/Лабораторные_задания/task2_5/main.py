list_ = [3, 4, 8, 9, 6, 6, 2, 4,5,5,5,3, 3]

count_even = 0  # количество четных чисел
count_odd = 0  # количество нечетных чисел

for A in list_:
    if A % 2 ==0:
        count_even = count_even + 1
    else:
        count_odd = count_odd +1
    print(count_even,count_odd)
if count_even > count_odd:
    print('Четных чисел больше')
else:
    print('Нечетных чисел больше')
