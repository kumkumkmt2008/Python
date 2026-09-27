def prime():
    num = int(input("Enter number: "))

    if num <= 1:
        print("Not prime")
    else:
        for i in range(2, num):
            if num % i == 0:
                print("Not prime")
                return

        print("Prime")

prime()