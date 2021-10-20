def task_1_1():
    max_sum = 500
    current_sum = 0
    n = 1
    while current_sum <= max_sum:
        current_sum += n**2
        if current_sum > max_sum:
            break
        else:
            print(n,current_sum)
            n = n + 1
    #1**2+2**2+3**3+....<=500

    return n


if __name__ == "__main__":
    # Write your solution here
    print(task_1_1())
