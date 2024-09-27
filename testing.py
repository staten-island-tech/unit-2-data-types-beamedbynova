variable = 5
if variable == 5:
    variable2 = 14
    print(variable2)

bill = 100
portionOfBill = bill / 100 * 15

print(portionOfBill)


# this code first asks for a number.
# it then creates a loop with a condition.
# if the number is greater than zero, the loop will print the number, and then subtract 1 from the number.
# it will continue to do this until the number no longer fufills the condition (if the number is greater than zero)
number = int(input("please input a number: "))
while number > 0:
    print(number)
    number = number - 1

type(14) == int
