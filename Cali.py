while True:
    try:
        first_num = int(input("First num you want to add?: "))
        second_num = int(input("Second num?: "))
        sum = first_num + second_num
        print("This is the number...:", sum)
        break
    except:
        print("Not a interger")