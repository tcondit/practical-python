# pcost.py
#
# Exercise 1.27 and 1.30


def portfolio_cost(filename):
    pcost = 0
    with open(filename, "rt") as f:
        header = next(f)
        for line in f:
            line = line.split(",")
            pcost = pcost + int(line[1]) * float(line[2])
    return pcost


pcost = portfolio_cost("Data/portfolio.csv")
print(f"portfolio cost: {pcost}")
