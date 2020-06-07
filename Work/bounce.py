# bounce.py
#
# Exercise 1.5

HEIGHT = 100  # meters

for bounce in range(1, 11):
    HEIGHT = round(HEIGHT * 0.6, 4)
    print(f"{bounce} {HEIGHT}")
