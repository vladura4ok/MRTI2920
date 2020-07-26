amount = 20000
years = 5
percent = 15

months = years * 12

income = amount * (1 + percent / (100 * 12) ) ** months
print(income)