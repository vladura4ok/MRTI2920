"""author - Бык Екатерина Николаевна"""
import math

a, b, c = 3, -14, -5

d = b*b-4*a*c
print(d)

x1 = (math.sqrt(d)-b) / (2*a)
x2 = (-math.sqrt(d)-b) / (2*a)

print(x1,x2)

print(a*x2*x2 + b*x2 + c)
