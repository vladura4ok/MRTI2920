Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a, b, c = 20000, 0.05, 60 #a-первоначальный вклад, b-годовая процентная ставка, с-количество месяцев(5 лет*12)
>>> d = a * ((1 + b / 12) ** c)
>>> print(int(d))
25667
>>> 