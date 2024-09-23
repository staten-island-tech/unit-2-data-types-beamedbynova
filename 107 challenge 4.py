# this is challenge 4 / the thing that accepts a bill value & offers a tip depending on the service quality.
# there's probably a more efficient way to write this code that uses less lines, but i have yet to find it.

bill = round(float(input("What is the bill? ")),2)
serviceQuality = (input("How was the customer service? Was the service great, good, okay, or bad? "))
if serviceQuality == "great":
    question1 = input("Would you like to leave a 25% tip? Y/N ")
    if question1 == "Y":
        tip1 = round(bill / 4, 2)
        total1 = round(bill + tip1,2)
        print(f"The bill is {bill}.")
        print(f"The tip is {tip1}.")
        print(f"The total price is {total1}.")
    else:
        print(f"The total price is {bill}.")
elif serviceQuality == "good":
    question2 = input("Would you like to leave a 20% tip? Y/N ")
    if question2 == "Y":
        tip2 = round(bill / 5, 2)
        total2 = round(bill + tip2,2)
        print(f"The bill is {bill}.")
        print(f"The tip is {tip2}.")
        print(f"The total price is {total2}.")
    else:
        print(f"The total price is {bill}.")
elif serviceQuality == "okay":
    question3 = input("Would you like to leave a 15% tip? Y/N ")
    if question3 == "Y":
        tip3 = round(bill / 100 * 15, 2)
        total3 = round(bill + tip3,2)
        print(f"The bill is {bill}.")
        print(f"The tip is {tip3}.")
        print(f"The total price is {total3}.")
    else:
        print(f"The total price is {bill}.")
elif serviceQuality == "bad":
    print(f"The total price is {bill}.")
else:
    print("error")