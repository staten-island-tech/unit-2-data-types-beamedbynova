# this is challenge 3 / a function that determines if a number is odd or even.

number = int(input("Please type a number: "))
oddOrEven = number % 2
if oddOrEven == 0:
    print("This number is even.")
else:
    print("This number is odd.")
