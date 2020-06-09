# pcost.py
#
# Exercise 1.27, 1.30, 1.31, 1.32, and 1.33

import csv
import sys


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


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"

# print(f"Using {filename}")
pcost = portfolio_cost(filename)
print(f"Total cost: {pcost}")
