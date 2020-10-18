from decimal import Decimal

m = 20000
y = 5
mon = y * 12
r = 0.15

D = m * ((1 + (r/12))**mon)
x = round (D, 2)
print(x)