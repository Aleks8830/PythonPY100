# TODO
A= int(input('Введите число 1: '))
B= int(input('Введите число 2: '))
C= int(input('Введите число 3: '))
if A < 45 and B >= 45 and C >= 45:
    print('истина')
elif A >= 45 and B < 45 and C >= 45:
    print('истина')
elif A >= 45 and B >= 45 and C < 45:
    print('истина')
else:
    print('ложь')