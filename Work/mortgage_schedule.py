# mortgage_schedule.py
#
# Exercise 1.10 and 1.17

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
    principal = (principal - extra) * (1 + rate / 12) - payment
    total_paid = total_paid + payment + extra
    months = months + 1
    print(f"{months:3d} {total_paid:10.2f} {principal:10.2f}")

print("Total paid", total_paid)
print("Number of months", months)
