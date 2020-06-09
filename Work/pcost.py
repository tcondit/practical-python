# pcost.py
#
# Exercise 1.27

pcost = 0
with open("Data/portfolio.csv", "rt") as f:
    header = next(f)
    for line in f:
        line = line.split(",")
        pcost = pcost + int(line[1]) * float(line[2])
print(f"portfolio cost: {pcost}")
