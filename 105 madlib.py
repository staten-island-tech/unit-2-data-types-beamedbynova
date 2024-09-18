# Madlib story:
# I'm sure you've heard the [adjective] story of George Washington and the [Noun] Tree. If you haven't, let me remind you. 
# When Washington was a young [noun], maybe around [number] year / years of age, his [adjective] father gifted him a very sharp [noun].
# "What a sharp [noun]!" Washington exclaimed excitedly. Washington's father was happy to see his son enjoying his gift.
# Washington was so excited to test out his brand new [noun], he walked right out of his [noun] and into the surrounding wilderness without telling his father anything!
# As he walked outside and away from his cozy [noun], he wondered what he should use his [noun] for. He kept walking as he pondered to himself, but eventually he stumbled upon his father's treasured [noun] tree. Of course, he did not know the tree was his father's.
# "Oh, joy! Something to test my sharp [noun] on!" Washington says to himself, readying the [noun] in his hand. He takes a mighty swing at the [noun] tree, his grip tightening on the [noun].
# BANG! The [noun] strikes the [noun] tree with an impact that could break your [noun]'s back. A jagged cut is left in the trunk of the [noun] tree where the [noun] struck. Satisfied with his [noun]'s preformance, he walks back to his [noun] with a wide smile on his face. 
# The next morning, Washingon's father sees the cut in his beloved [noun] tree and is angered. When he asked Washington what happened to the tree, he bravely answered:
# "I cannot tell a lie. Yes father, I did cut the [noun] tree with my sharp [noun]."
# Washington's father embraces his son with a tight hug, saying that his son's honesty was worth a thousand [noun] trees.
# And that's the story of George Washington and the [noun] tree. I hope this story brought you the same feelings of [noun] that it brought me. And of course, a story isn't complete without a theme. This story teaches the beautiful lesson that honesty is always the most honorable thing someone can dsplay.

# The sp

quizStart = input("You are about to take a quiz on one of the oldest myths in American history. Type 'Yes' to continue. ")
if quizStart == "Yes":
    disclaimer = input("Disclaimer: the answers in this quiz do not have to be accurate. There are no 'wrong' answers when it comes to this quiz, so you can answer with anything you want. Type 'I understand' to continue. ")
    if disclaimer == "I understand":
        tree = input("George Washington was the first president of the United States. There is a popular myth surrounding him related to a tree; what was the tree featured in the myth? (respond with a noun) ")
        washingtonYoung = input("What is Washington? (respond with a noun) ")
        washingtonAge = input("How old is Washington in the story? ")
        washingtonFather = input("How would you describe Washington's father? (respond with an abstract noun) ")
        washingtonGift = input("In the story, Washington's father gave him a gift. What was the gift? (respond with a noun) ")
        washingtonHouse = input("What does Washington live inside of? (respond with a noun) ")
        
    else:
        print("You have not agreed to the terms.")
else:
    print("You have not typed 'Yes.' Please try again by running the code.")

    
# notes:
# some nouns should share a variable value. for example, the gift washington recieves would have the same variable throughout the story.
# maybe you could format this story as a quiz, and the plot twist is that the program is actually a madlib. if you go with the quiz idea, let the reader know that the answers can be as wacky as possible.