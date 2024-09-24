# this is challenge 5 / the code that lists all of the factors of a number.

number = int(input("please input a number: "))
divisor = 1
factorList = []
while divisor < number:
    dividend = number % divisor
    divisor = divisor + 1
    if dividend == int:
        factorList.append(dividend)
    else:
        print("nothing")
print(factorList)


# to make this:
# get a number
# divide it by a certain number and see if it leaves a remainder
# if the output does not have a remainder, put it into a list
# continue this until the divisor is greater than the number
# print out all of the numbers that did not leave a remainder