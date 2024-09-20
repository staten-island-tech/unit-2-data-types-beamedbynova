# this is challenge 2 / the madlib project. this madlib starts off as a quiz, and then retells the story of "george washington and the cherry tree" using your answers.

quizStart = input("You are about to take a quiz on one of the oldest myths in American history. Type 'Yes' to continue. ")
if quizStart == "Yes":
    disclaimer = input("Disclaimer: the answers in this quiz do not have to be accurate. There are no 'wrong' answers when it comes to this quiz, so you may answer however you want. I would advise against using the letter 'a' in your responses, though. Type 'I understand' to continue. ")
    if disclaimer == "I understand":
        tree = input("George Washington was the first president of the United States. There is a popular myth surrounding him related to a tree; what was the tree featured in the myth? (respond with a noun, don't respond with the word tree) ")
        washingtonSpecies = input("What is Washington? (respond with a noun) ")
        washingtonAge = int(input("How old is Washington in the story? "))
        washingtonFather = input("How would you describe Washington's father? (respond with an abstract noun) ")
        washingtonGift = input("In the story, Washington's father gives him a gift. What was the gift? (respond with a noun) ")
        washingtonHouse = input("What does Washington live inside of? (respond with a noun) ")
        storyConfirm = input("The quiz is now over. Type 'Proceed' to see the retelling of 'George Washington and the " + tree + " tree,' according to your answers. ")
        Madlib = f"When Washington was a young {washingtonSpecies} (about {washingtonAge} years old), his {washingtonFather} father gifted him a very sharp {washingtonGift}. 'Wow! What a sharp {washingtonGift}!' Washington exclaims, stunned as he looks at the gift in his hands. Washington's father was happy to see his son satisfied with his gift, and he left the room to go cook some food. Washington was very eager to use his new {washingtonGift}; in fact, he was so eager that he walked right out of his {washingtonHouse} without letting his father know! As he walked around the wilderness surrounding his {washingtonHouse}, he wondered what he could test his brand new {washingtonGift} on. Eventually, something catches his eye: A humble {tree} tree that even a {washingtonAge} year old could cut down! Washington clutches his {washingtonGift} in his hand and takes a mighty swing at the {tree} tree. BANG! The {washingtonGift} crashes into the {tree} tree, leaving a large gap in the trunk. Satisfied with his {washingtonGift}'s preformance, he walks back to his {washingtonHouse} and goes to sleep. The next morning, Washington's father calls him outside and brings him to the {tree} tree. 'George, why is there a large gap in the trunk of my {tree} tree?' he asks furiously. 'I cannot tell a lie, father. I was the one who tried to cut the tree,' Washington responds bravely. His father's anger vanishes within an instant, and he hugs his son tightly. 'Your honesty is worth a thousand {tree} trees,' he says."
        if storyConfirm == "Proceed":
            print(Madlib)
        else:
            print("You have not typed 'Proceed' correctly. Please try again by running the code.")
    else:
        print("You have not agreed to the terms.")
else:
    print("You have not typed 'Yes.' Please try again by running the code.")
