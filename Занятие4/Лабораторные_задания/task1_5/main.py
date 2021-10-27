if __name__ == "__main__":
    list_ = [41, -13, 10, -1, 32, -3, -6, 8, 6, 9, 3]
    even = 0
    odd = 0
    for i in list_:
        if i %2 ==0:
            even += 1
        else:
            odd+=1
if odd > even:
    print("odd")
else:
    print("even")

