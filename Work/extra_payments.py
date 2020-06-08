# extra_payments.py
#
# Exercise 1.8

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0

while principal > 0:
    if months < 12:
        extra_payment = 1000
    else:
        extra_payment = 0
    principal = (principal - extra_payment) * (1 + rate / 12) - payment
    total_paid = total_paid + payment + extra_payment
    months = months + 1

print("Total paid", total_paid)
print("Number of months", months)
