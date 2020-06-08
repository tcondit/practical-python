# mortgage_schedule_overpayment.py
#
# Exercise 1.11

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0
extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    if months >= extra_payment_start_month and months < extra_payment_end_month:
        extra = extra_payment
    else:
        extra = 0

    if payment > principal:
        principal = 0
        total_paid = total_paid + principal
    else:
        principal = (principal - extra) * (1 + rate / 12) - payment
        total_paid = total_paid + payment + extra
    months = months + 1
    print(f"{months:2d} {total_paid:.2f} {principal:.2f}")

print()
print(f"Total paid {total_paid:.2f}")
print("Number of months", months)
