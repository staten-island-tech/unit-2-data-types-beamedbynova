# to make a word counter:
# get user input
# split the user input into a list
# make something that counts the amount of words in the list
# print that value out

# you can have multiple data types in a print command, just separate the data types with commas

# this code currently takes the inputted sentence and prints out a list with all of the words.
# add some form of counter
sentence = input("type out a sentence: ")
wordList = sentence.split()
print("this is the word list:", wordList)