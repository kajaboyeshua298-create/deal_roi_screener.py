starting_cash = float(input("Enter starting cash in dollars: "))
annual_return = float(input("Enter annual return percent: "))
years = int(input("Enter number of years: "))

future_value = starting_cash * (1 + annual_return / 100) ** years
print("Future Value ($):", round(future_value, 2))

if future_value >= 100000:
    print("Goal reached!")
else:
    print("Goal unreached.")
