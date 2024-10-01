# this is challenge 6 / a function that finds the greatest common factor of two numbers

a = int(input("Input your first number: ")) # first number
b = int(input("Input your second number: ")) # second number
listOfNumbers = [] # list that takes all of the common factors

def greatestCommonFactor(x, y): # defines function to find gcf
    for i in range(1, b + 1): # for loop that has every number from 1 to b
        if x % i == 0 and y % i == 0: # if statement that requires x and y to both be 0 after a modulo
            listOfNumbers.append(i) # if both x and y are 0, its added to the list
    print(max(listOfNumbers)) # prints the last number in the list, the gcf
greatestCommonFactor(a,b) # calls function
