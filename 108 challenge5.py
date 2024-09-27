# this is challenge 5 / the code that lists all of the factors of a number.

# this code is copied and pasted from google because i was stuck on this challenge. to compensate, i wrote an explanation of the code to make sure i wasnt confused on anything. these notes are mostly for me to reread to understand, though.
# this defines a function that prints the factors of a number.
# the print line prints text that details what the list of numbers are.
# the for loop starts at the first value in the () and ends right before the second one. this is because the for loop accepts two arguments. the reason why the range command must have 2 arguments is because the loop iterates itself x - 1 amount of times, with x being the last argument in the for loop. in this case, the loop would start at 1, and then ends at x because it includes x, but not x + 1.
# loops will always end before the last argument because "0" is considered an element. programming tends to use the set of whole numbers, and 0 is a whole number at the start of the list. 
# the if statement says at if the remainder of x % i is equal to 0, it would be printed. this is because anything that divides into a number cleanly without a remainder is automatically a factor of that number.
# note that there is no "else" part connected to the if statement. this tells the code to ignore any other output and discard it.
# the last line prints out all the numbers that divide evenly into the entered number.
# 
num = int(input("please input a number: "))
def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)
print_factors(num)

# range(1) = starts at 0, ends before
# range(0) doesnt do anything
# you dont have to enter the values in a list, you can just have them printed out in the console.
# dont overcomplicate things


number = int(input("Enter a number: "))
def print_factors2(x):
    for i in range(1, x+1):
        if x % i == 0:
            print(i)
print_factors2(number)

# split things into smaller bits until everything is digestible