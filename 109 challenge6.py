# this is challenge 6 / a function that finds the greatest common factor of two numbers

a = int(input("Input your first number: "))
b = int(input("Input your second number: "))
listOfNumbers = []

def greatestCommonFactor(x, y):
    for i in range(1, b + 1):
        if a % i == 0 and b % i == 0:
            listOfNumbers.append(i)
    print(listOfNumbers[-1])
greatestCommonFactor(a,b)

# 