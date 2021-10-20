if __name__ == "__main__":
    # Write your solution here
    list_=[2,4,6,4,3,3,5,6,7,8,9,0,7,6,]
    i = list_.index(max(list_))
    list_[0], list_[i] = list_[i], list_[0]
    print(list_)