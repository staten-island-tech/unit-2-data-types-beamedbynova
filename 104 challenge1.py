# to make a word counter:
# get user input
# split the user input into a list
# make something that counts the amount of words in the list
# print that value out
# you can have multiple data types in a print command, just separate the data types with commas

# Class Notes:
# for .split() commands, you enter the variable to let the code know what string to split.
# use "len" to count the amount of elements / characters in a string.
# use "x.count('y')" to count the amount of times y appears in the string. since it is stored as an int/flt, it can undergo mathematical operation.
# use "elif" for remaining cases in an if statement. "elif" is shorthand for "else if"

# Code Notes:
# this code first asks for user input, asking for the user to type out a sentence.
# once the user types the sentence, the code will store the sentence in the variable of the same name.
# it will then split all of the words in said sentence and store it in the variable "wordList."
# the code will then count the amount of words in the string using "len" and store it in the variable "countOfWords."
# the code also counts the amount of letters in the stored string and stores it in the variable "countOfLetters."
# the "sentence.count(' ')" portion lets the code know to count the amount of spaces in the sentence and subtract it from the total amount of characters.
# the print commands print out the word list and the count of words.

# reminders:
# make if statements to change the sentence if countOfWords is equal to 1
# do the same for the amount of letters.
sentence = input("Type out a sentence: ")
wordList = sentence.split()
countOfWords = len(wordList)
countOfLetters = len(sentence) - sentence.count(' ')
if countOfWords == 1:
    print("There is one word in this sentence.")
else:
    print("There are",countOfWords,"words in this sentence.")

if countOfLetters == 1:
    print("There is one letter in this 'sentence.'")
else:
    print("There are",countOfLetters,"letters in this sentence.")
