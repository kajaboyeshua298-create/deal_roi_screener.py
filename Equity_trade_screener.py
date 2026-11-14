buy_price = float(input("Enter buy price: "))
sell_price = float(input("Enter sell price: "))
number_shares = float(input("Enter number of shares: "))
goal = float(input("Enter your end goal:"))

net_profit = (sell_price - buy_price) * number_shares
percent_return = ((sell_price - buy_price) / buy_price) * 100
print()
print()
print(f"Net Profit: ${net_profit:,.2f}")
print(f"Percentage Return: {percent_return:.2f}%")
print()

if  net_profit >= goal:
    print("Target goal reached!")
elif net_profit > 0:
    print("Trade profitable, but below target goal.")
else:
    print("Trade resulted in a loss or break-even.")
