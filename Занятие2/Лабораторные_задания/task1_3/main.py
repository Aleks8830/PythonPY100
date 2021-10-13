# TODO
A = int(input("Введите число А: "))
B = int(input("Введите число B: "))
Sun_kv = A*A+B*B
KV_sum= (A+B)*(A+B)
if Sun_kv < KV_sum:
    print("Сумма квадратов больше квадрата суммы")
else:
    print("квадрат суммы больше суммы квадратов")