if __name__ == "__main__":
    # Write your solution here
    num = int(input("ВВедите число "))
    list_1 = [int(i)for i in str(num)]
    print("1.Cписок цифр: ",list_1)
    print("2.Сумма всех цифр:", sum(list_1))
    odd = [int(i) for i in list_1 if i %2 ==0]
    print("3. Найти сумму всех четных чисел:  ",sum(odd))


    pass
