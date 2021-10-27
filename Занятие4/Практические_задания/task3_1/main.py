if __name__ == "__main__":
    cart = {
        "apple": 80,
        "orange": 65,
        "banana": 40
    }

    # TODO посчитать через ключи
    sum = 0
    for fruit in cart:
        sum+=cart[fruit]
        print(fruit, cart[fruit])  # получаем значение по ключу
    print(sum)
    # TODO посчитать через метод values
  #  sum (cart.values())
  # cart.items()