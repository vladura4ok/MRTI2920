money = float(input('введите сумму вклада, BYN '))
month = int(input('введите период, в месяцах '))
per = float(input('годовой процент,% '))

dep = money * (1 + per / (12 * 100)) ** month
print("-----", "Ежемесячная капитализация. ", "-----")
print("Ориентировочная сумма на счету в конце указанного срока", round(dep, 2), "BYN")
print("Сумма начисленных %", round(dep - money, 2), "BYN")
