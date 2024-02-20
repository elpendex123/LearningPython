print("bill calculator")

bill = float(input("total bill? "))

tip = float(input("percentage tip? "))

split = float(input("number of people to split with? "))

pay = "{:.2f}".format(round(bill * (1 + tip / 100) / split, 2))

print(f"each person to pay: {pay}")