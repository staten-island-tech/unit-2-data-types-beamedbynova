# this is challenge 6 / a function that finds the greatest common factor of two numbers

a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))

def gcf(x, y): # defines a function that requires 2 values
    for i in range(a, b + 1): # loop that finds the remainder of all the values 
        if a % i == 0 and b % i == 0: # if statement where the remainders of both a and b have to equal zero
            print(i) # if the conditions are fufilled, it will print the shared remainder

gcf(a, b) # the two values for this function are the inputted values above

# get two inputted values (done)
# define a function that takes these two values (done)
# create a for loop that would modulo both inputted values
# make it so that if the inputted values share a remainder, make it print it out
# make it so that if no remainders are shared, print only 1