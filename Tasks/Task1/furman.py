a = int(input("Введите сумму (рубли): "))
b = int(input("Введите процет дипозита: "))
z = int(input("Введите срок дипозита (годы): "))
before = 100 * a
after = int(before * (100 + z*b) / 100)
print(after // 100)
