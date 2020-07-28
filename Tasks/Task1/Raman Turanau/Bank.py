from decimal import Decimal

money = int(input("введите сумму вклада: "))
years = int(input("введите срок вклада в годах: "))
rate = int(input("введите годовую процентную ставку: "))
monthly_rate = Decimal(rate / 12)
months = years * 12
answer = money * (1 + monthly_rate / 100) ** months
answer2 = str(answer.quantize(Decimal("1.00")))
print ("вы получите " + answer2 + " денег"  )