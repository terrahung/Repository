# Day 3 Practice 5 - Python Pizza (Angela Yu's code for reference)

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L:")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# todo: work out how much they need to pay based on their size choice.
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You typed the wrong inputs.")
# Todo: work out how much they need to pay based on their pepperoni choice.
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
# Todo: work out how much they need to pay based on their extra cheese choice.
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")