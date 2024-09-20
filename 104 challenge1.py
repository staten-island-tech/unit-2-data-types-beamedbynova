# this is challenge 1 / the word counter.

# Class Notes:
# for .split() commands, you enter the variable to let the code know what string to split.
# use "len" to count the amount of elements / characters in a string.
# use "x.count('y')" to count the amount of times y appears in the string. since it is stored as an int/flt, it can undergo mathematical operation.
# use "elif" for remaining cases in an if statement. "elif" is shorthand for "else if"

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
