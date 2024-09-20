bill = float(input("What is the bill? "))
serviceQuality = (input("How was the customer service? Was the service great, good, okay, or bad? "))
if serviceQuality == "great":
    tip1 = input("would you like to leave a 25% tip? Y/N ")
    if tip1 == "Y":
        
elif serviceQuality == "good":
    print("good")
elif serviceQuality == "okay":
    print("okay")
elif serviceQuality == "bad":
    print("bad")
else:
    print("error")

# create a func to accept a "bill" value
# also ask the user if they want to leave a tip
# calculate the price

# get the bill amount, divide it by whatever the percent tip is in fraction form