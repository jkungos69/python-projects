while True:
    try:
        user_name = int(input("Input a number: "))

        if user_name == 7:
            print("Tumpak ! Malingat  ka lang nahulaan mo rin")
            break 
        else:
            print("Mali, hula ulit!")
    except ValueError:

        print("Mali, hula ulit!")