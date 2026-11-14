company_valuation = float(input("Enter buy price: "))
annual_ebitda = float(input("Enter annual EBITDA (operating profit): "))
ev_ebitda = company_valuation / annual_ebitda

print()
print(f"EV/EBITDA Multiple: {ev_ebitda:.2f}x")

if ev_ebitda <= 6:
    print("Cheap Buyout Target!")
elif ev_ebitda <= 10: 
    print("Fair Valuation")
else:
    print("Too Expensive - Pass")
