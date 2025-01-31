def mortgage_payments(principal, rate, amortization):
    rq = rate / 100
    r_monthly = (1 + rq / 2) ** (2 / 12) - 1
    r_semi_monthly = (1 + rq / 2) ** (2 / 24) - 1
    r_bi_weekly = (1 + rq / 2) ** (2 / 26) - 1
    r_weekly = (1 + rq / 2) ** (2 / 52) - 1

    n_monthly = amortization * 12
    n_semi_monthly = amortization * 24
    n_bi_weekly = amortization * 26
    n_weekly = amortization * 52

    def PVA(r, n):
        return (1 - (1 + r) ** -n) / r

    monthly_payment = principal / PVA(r_monthly, n_monthly)
    semi_monthly_payment = principal / PVA(r_semi_monthly, n_semi_monthly)
    bi_weekly_payment = principal / PVA(r_bi_weekly, n_bi_weekly)
    weekly_payment = principal / PVA(r_weekly, n_weekly)
    rapid_bi_weekly_payment = monthly_payment / 2
    rapid_weekly_payment = monthly_payment / 4

    return (
        round(monthly_payment, 2),
        round(semi_monthly_payment, 2),
        round(bi_weekly_payment, 2),
        round(weekly_payment, 2),
        round(rapid_bi_weekly_payment, 2),
        round(rapid_weekly_payment, 2)
    )

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the quoted interest rate: "))
amortization = int(input("Enter the amortization period: "))

payments = mortgage_payments(principal, rate, amortization)

print("\nMortgage Payment Breakdown:")
print(f"Monthly Payment: ${payments[0]:,.2f}")
print(f"Semi-monthly Payment: ${payments[1]:,.2f}")
print(f"Bi-weekly Payment: ${payments[2]:,.2f}")
print(f"Weekly Payment: ${payments[3]:,.2f}")
print(f"Rapid Bi-weekly Payment: ${payments[4]:,.2f}")
print(f"Rapid Weekly Payment: ${payments[5]:,.2f}")

