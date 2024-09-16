# a "string" is a data type that refers to text.
# strings aren't words, they are instead characters in a list.
# this detail is important because it allows a print command to only print specific parts of a string.
# it also allows 

# this loop prints the first 6 letters of "square". the word "squares" is tied to a variable.
word = "squares"
#for i in range(6):
    #print(word[i])

# x has a string attached to it as a value since it is a variable.
# y's value is the string attached to x formatted as a list.
# the x.split() portion splits the string into a list.
# z's value is the first word within y's list. in this case, the value of z would be "this".
x = "this is a thing"
y = x.split( )
z = y[0]
print(y)

