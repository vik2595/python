def myfun():
    print("welcome to my calc")

    a = int(input("enter first num:"))
    b = int(input("enter second num:"))

    print("1. Sum \n2. Multi \n3. Div \n4. sub")

    choice = int(input("Select your choice: "))

    if choice == 1:
        print(a + b)
    elif choice == 2:
        print(a * b)
    elif choice == 3:
        print(a/b)
    elif choice == 4:
        print(a - b)
    else:
        print("Try again:\n")
        return myfun()


myfun()
