total_loan = 320000
final_gp = 73.5
graduated_on_time = True
ib_monthly_savings =28000

if  final_gp >= 70 and graduated_on_time == True:
    forgiven_amount = total_loan * 0.50
    status = "50% ACADEMIC FORGIVENESS UNLOCKED"

else:
    forgiven_amount = 0
    status = "Full Debt Owed"
remaining_loan = total_loan - forgiven_amount
months_to_payoff = round(remaining_loan/ib_monthly_savings,1)
print(total_loan)
print(status)
print(forgiven_amount)
print(remaining_loan)
print(months_to_payoff)
