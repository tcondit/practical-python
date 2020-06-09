# pcost.py
#
# Exercise 1.27, 1.30, and 1.31

# Modify the pcost.py program to catch the exception, print a warning message, and continue processing the rest of the file.


def portfolio_cost(filename):
    pcost = 0
    with open(filename, "rt") as f:
        header = next(f)
        for line in f:
            line = line.split(",")
            try:
                pcost = pcost + int(line[1]) * float(line[2])
            except ValueError:
                print(f"Couldn't parse {line}")
    return pcost


pcost = portfolio_cost("Data/portfolio.csv")
print(f"Total cost: {pcost}")
