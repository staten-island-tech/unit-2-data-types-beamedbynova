# there are various data types in all languages, understanding the differences between them are very important.
# integers = whole numbers
# floats = numbers with decimal values
# strings = words for an output. use quotes

# both integers and strings can have the same output, but they are different
# it is important to convert strings into integers to preform mathematical operations

# the "float(x)" lets the value tied to y be a decimal value. 
# x can only be a whole number since the "float(x)" command is not present.
x = 3
y = float(3)

# integers and floats can be put into a list, or set, that is then printed out.
# different data types can be stored in a list.
# "data types" is used to refer to both integers and floats.

# the loop in this code prints out each individual number within the list.
# "i" represents the amount of values in the list, "values" represents the list itself.
# this causes the loop to print each number in the list individually.
values = [1,2.23,5,7,2,30,15]
for i in values:
    print(i)

# to get a specific element in the set, use [] brackets and use the position of the element in the list.
# always start counting from 0 intead of 1.

# this print command prints the "0th" term in the list, or the number 1.
print(values[0])