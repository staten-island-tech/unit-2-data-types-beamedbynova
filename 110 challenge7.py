#this is challenge 7 / the tip calculator

price = float(input("What is the bill? ")) # og price
tip = int(input("What is the tip percentage? ")) # tip percent
tipAmount = price / 100 * tip # how much extra ur paying
total = round(price + tipAmount, 2)

print(f"The total is {total}.")