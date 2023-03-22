x = int(input("Enter number:"))
check = True

if x == 1:
    print(x, "is not a prime number")
elif x > 1:
    for y in range(2, x):
        if (x % y) == 0:
            check = False
            break

    if check:
        print(x, "is a prime number")
    else:
        print(x, "is not a prime number")




