deposit = 20000
years = 5
month = 12
percents = 5

kap = 1 + ((percents / month) / 100)
deposit = round(deposit * pow(kap, (years * month)), 2)
print(deposit)
