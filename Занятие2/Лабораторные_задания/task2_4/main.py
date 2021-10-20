if __name__ == "__main__":
    # постарайтесь не использовать "магические" числа,
    # а по возможности дать переменным осмысленные названия и использовать их
    text = 'Hello,world'
    ots = "     "
    for i in range(0,len(text)):

        print(ots,text[i])
        ots += ' '

    #for index, value in enumerate(text):
      #  print(index,value)
    #print(prod)
