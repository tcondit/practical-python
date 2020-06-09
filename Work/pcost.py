# pcost.py
#
# Exercise 1.27, 1.30, 1.31, and 1.32

import csv


def portfolio_cost(filename):
    pcost = 0
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        _ = next(rows)  # remove header
        for row in rows:
            try:
                pcost = pcost + int(row[1]) * float(row[2])
            except ValueError:
                print(f"Couldn't parse {row}")
    return pcost


pcost = portfolio_cost("Data/portfolio.csv")
print(f"Total cost: {pcost}")
