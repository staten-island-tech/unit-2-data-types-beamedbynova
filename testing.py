a = int(input("Input your first number: "))
b = int(input("Input your second number: "))

def greatestCommonFactor(x, y):
    for i in range(1, b + 1):
        if x % i == 0 and y % i == 0:
            print(i)
greatestCommonFactor(a,b)